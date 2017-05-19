"""Module to translate a MEN file."""
import os
import logging
import importlib

import mumen.utils.constants as const


__all__ = ['translate_dataset']

logger = logging.getLogger(__name__)


def _translate_entry(entry, target_lang_iso_1, config):
    logger.debug('Loading translator: {}_{}.py'.format(config['from'],
                                                       target_lang_iso_1))
    translator = importlib.import_module(
        'mumen.translation.translators.{}_{}'.format(config['from'],
                                                     target_lang_iso_1))
    return getattr(translator, 'translate')(entry, target_lang_iso_1, config)


def _translate_tuple(input_tuple, target_lang_iso_1, config):
    logger.info('Translating tuple: {}'.format(input_tuple))
    return (_translate_entry(input_tuple[0], target_lang_iso_1, config),
            _translate_entry(input_tuple[1], target_lang_iso_1, config))


def _translate_dataset(source_stream, target_lang_iso_1, config):
    """Returns a list of tuples."""
    translated_tuples = []
    for line in source_stream:
        tab_split = line.strip().split(const.WSPACE)
        _translated_tuple = _translate_tuple((tab_split[0], tab_split[1]),
                                            target_lang_iso_1,
                                            config)
        logger.info('Translated tuple: {}'.format(_translated_tuple))
        translated_tuple = []
        translated_tuple[0] = _translated_tuple[0]
        logger.info('Translated tuple: {}'.format(translated_tuple))
        translated_tuples.append(translated_tuple)
    #logger.debug(trans_tuples)
    return translated_tuples


def translate_dataset(target_lang_iso_1, config):
    """Translate a whole MEN dataset from a source language to a target
    language and print to file."""
    logger.debug('Translating dataset: {}'.format(config['datasets']['source']))
    logger.debug('  from: {}'.format(config['from']))
    logger.debug('  to: {}'.format(target_lang_iso_1))
    os.makedirs(os.path.dirname(config['datasets']['target']),
                                exist_ok=True)
    with open(config['datasets']['source'], 'r')as source_stream,\
         open(config['datasets']['target'], 'w') as target_stream:

        logger.debug('Saving translations to output file: {} '.format(target_stream))
        print(const.NEW_LINE.join(_translate_dataset(source_stream,
                                                     target_lang_iso_1,
                                                     config)),
              file=target_stream)
