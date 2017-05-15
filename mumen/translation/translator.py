"""Module to translate a MEN file."""
import logging
import importlib

import mumen.utils.constants as const


__all__ = ['translate_dataset']

logger = logging.getLogger(__name__)


def _translate_entry(entry, target_lang_iso_1, config):
    translator = importlib.import_module(
        'mumen.translation.translators.{}_{}'.format(config['from'],
                                                     target_lang_iso_1))
    return getattr(translator, 'translate')(entry, target_lang_iso_1, config)


def _translate_tuple(input_tuple, target_lang_iso_1, config):
    return (_translate_entry(input_tuple[0], target_lang_iso_1, config),
            _translate_entry(input_tuple[1], target_lang_iso_1, config))


def _translate_dataset(source_stream, target_lang_iso_1, config):
    """Returns a list of tuples."""
    trans_tuples = []
    for line in source_stream:
        tab_split = line.split(const.TAB)
        trans_tuples.append(_translate_tuple((tab_split[0], tab_split[1]),
                                             config['from'],
                                             target_lang_iso_1))
    return trans_tuples


def translate_dataset(target_lang_iso_1, config):
    """Translate a whole MEN dataset from a source language to a target
    language and print to file."""
    with open(config['datasets']['source'], 'r')as source_stream,\
         open(config['datasets']['target'], 'w') as target_stream:

        print(const.NEW_LINE.join(_translate_dataset(source_stream,
                                                     target_lang_iso_1,
                                                     config)),
              file=target_stream)
