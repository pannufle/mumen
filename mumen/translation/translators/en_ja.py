"""Translate from English to Japanese."""
import logging
import importlib
from collections import defaultdict
from functools import reduce


__all__ = ['translate']

logger = logging.getLogger(__name__)


def _get_first_element(translation_set):
    for item in translation_set:
        logger.debug('Returning item: {}'.format(item))
        return item


def _translate_lemma(lemma, target_lang_iso_1, config):
    translations = defaultdict(list)
    for dict_name, dict_config in config['dictionaries'].items():
        if dict_config['use']:
            dictionary = importlib.import_module(
                'mumen.translation.dictionaries.{}'.format(dict_name))
            translations[dictionary].extend(
                getattr(dictionary, 'get_translations')(lemma,
                                                        target_lang_iso_1,
                                                        config))
    return translations


def translate(entry, target_lang_iso_1, config):
    """Translate the entry from English to Japanese"""
    # TODO: detect whether entry is word or lemma (with pos)
    translations_dict = _translate_lemma(entry, target_lang_iso_1, config)
    intersect = reduce(set.intersection, (set(val) for val in translations_dict.values()))
    logger.debug('Intersection = {}'.format(intersect))
    return _get_first_element(intersect)
