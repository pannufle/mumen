"""Module to translate a MEN file."""
import os
import logging
import importlib

import mumen.utils.constants as const
from mumen.models.mentry import MENtry


__all__ = ['translate_dataset']

logger = logging.getLogger(__name__)


def _translate_entry(entry, target_lang_iso_1, config):
    logger.debug('Loading translator: {}_{}.py'.format(config['from'],
                                                       target_lang_iso_1))
    translator = importlib.import_module(
        'mumen.translation.translators.{}_{}'.format(config['from'],
                                                     target_lang_iso_1))
    return getattr(translator, 'translate')(entry, target_lang_iso_1, config)


def _translate_mentry(mentry, target_lang_iso_1, config):
    logger.info('Translating MENtry: {} {}'
                .format(mentry.pair.first, mentry.pair.last))
    translated_first = _translate_entry(mentry.pair.first,
                                        target_lang_iso_1, config)
    translated_last = _translate_entry(mentry.pair.last,
                                       target_lang_iso_1, config)
    return MENtry(translated_first, translated_last)


def _translate_dataset(source_stream, target_lang_iso_1, config):
    """Return a list of MENtries (MENtry objects)."""
    translated_mentries = []
    for line in source_stream:
        splits = line.strip().split()
        mentry = MENtry(splits[0], splits[1], splits[2])
        translated_mentry = _translate_mentry(mentry,
                                              target_lang_iso_1,
                                              config)
        logger.info('Translated MENtry: {} {}'
                    .format(translated_mentry.pair.first,
                            translated_mentry.pair.last))
        translated_mentries.append(translated_mentry)
    return translated_mentries


def _get_accuracy_metrics(mentries):
    errors = 0
    for mentry in mentries:
        if mentry.pair.first == mentry.pair.last:
            errors += 1
    return errors


def _get_recall_metrics(mentries):
    total_num_words = 0
    total_num_nones = 0  # Failed translations
    for mentry in mentries:
        if not mentry.pair.first:
            total_num_nones += 1
        if not mentry.pair.last:
            total_num_nones += 1
        total_num_words += 2
    total_sucess_translations = total_num_words - total_num_nones
    return (total_sucess_translations, total_num_words)


def translate_dataset(target_lang_iso_1, config):
    """Translate a whole MEN dataset from a source language to a target language
    and print to file.
    """
    logger.debug('Translating dataset: {}'.format(
        config['datasets']['source']))
    logger.debug('  from: {}'.format(config['from']))
    logger.debug('  to: {}'.format(target_lang_iso_1))
    os.makedirs(os.path.dirname(config['datasets']['target']),
                exist_ok=True)
    with open(config['datasets']['source'], 'r')as source_stream,\
            open(config['datasets']['target'], 'w') as target_stream:

        logger.debug(
            'Saving translations to output file: {} '.format(target_stream))
        translated_mentries = _translate_dataset(source_stream,
                                                 target_lang_iso_1,
                                                 config)
        coverage = _get_recall_metrics(translated_mentries)
        logger.info('{} words translated out of {}'.format(coverage[0],
                                                           coverage[1]))

        num_errors = _get_accuracy_metrics(translated_mentries)
        logger.info(
            '{} errors out of {} entries'.format(num_errors,
                                                 len(translated_mentries)))

        accuracy = ((len(translated_mentries) - num_errors) /
                    len(translated_mentries)) * 100
        recall = (coverage[0] / coverage[1]) * 100
        f1_score = ((accuracy * recall) / (accuracy + recall)) * 2

        logger.info('Accuracy = {}%'.format(round(accuracy, 1)))
        logger.info('Recall = {}%'.format(round(recall, 1)))
        logger.info('F1 = {}%'.format(round(f1_score, 1)))

        print(const.NEW_LINE.join(['{} {}'.format(trans.pair.first,
                                                  trans.pair.last)
                                   for trans in translated_mentries]),
              file=target_stream)
