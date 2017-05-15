"""Module to translate a MEN file."""
import logging
import importlib

import mumen.utils.constants as const


__all__ = ['translate_dataset']

logger = logging.getLogger(__name__)


def _translate_entry(entry, source_lang_iso_1, target_lang_iso_1):
    translator = importlib.import_module(
        'mumen.translation.translators.{}_{}'.format(source_lang_iso_1,
                                                     target_lang_iso_1))
    return getattr(translator, 'translate')(entry)


def _translate_tuple(input_tuple, source_lang_iso_1, target_lang_iso_1):
    return (_translate_entry(input_tuple[0], source_lang_iso_1,
                             target_lang_iso_1),
            _translate_entry(input_tuple[1], source_lang_iso_1,
                             target_lang_iso_1))


def _translate_dataset(target_lang_iso_1, source_stream, config):
    """Returns a list of tuples."""
    trans_tuples = []
    for line in source_stream:
        tab_split = line.split(const.TAB)
        trans_tuples.append(_translate_tuple((tab_split[0], tab_split[1]),
                                             config['from'],
                                             target_lang_iso_1))
    return trans_tuples


def translate_dataset(lang_iso_code, config):
    """Translate a whole MEN dataset from a source language to a target
    language and print to file."""
    with open(config['datasets']['source'], 'r') as source_stream,\
         open(config['datasets']['target'], 'w') as target_stream:

        print(const.NEW_LINE.join(_translate_dataset(lang_iso_code,
                                                     source_stream,
                                                     config)),
              file=target_stream)
