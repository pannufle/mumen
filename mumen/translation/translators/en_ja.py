"""Translate from English to Japanese."""
import logging
import importlib
from collections import defaultdict

import mumen.utils.constants as const


__all__ = ['translate']

logger = logging.getLogger(__name__)


def _translate_lemma(lemma, target_lang_iso_1, config):
    translations = defaultdict(list)
    partition = lemma.rpartition(const.HYPHEN)
    word = partition[0]
    pos = partition[2]
    for dict_name, dict_config in config['dictionaries'].items():
        if dict_config['use']:
            dictionary = importlib.import_module(
                'mumen.translation.dictionaries.{}'.format(dict_name))
            translations[dictionary].extend(
                getattr(dictionary, 'get_translations')(word,
                                                        pos,
                                                        target_lang_iso_1,
                                                        config))
    return translations


def translate(entry, target_lang_iso_1, config):
    """Translate the entry from English to Japanese"""
    # TODO: detect whether entry is word or lemma (with pos)
    translations_dict = _translate_lemma(entry, target_lang_iso_1, config)
    return ''
