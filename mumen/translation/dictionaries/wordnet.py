"""WordNet Translator.

Module to translate both words using wordnet.
"""
import logging

import nltk.corpus.wordnet as wn
import mumen.utils.constants as const

__all__ = ['get_translations']

logger = logging.getLogger(__name__)


def get_translations(word, pos, target_lang_iso_1, config):
    """Get WordNet translations of word (with pos) from source to target
    language"""
    translations = []
    # TODO: Add validation for languages
    source_lang_iso_2 = const.LANG_ISO_639_1_TO_2_DICT[config['from']]
    target_lang_iso_2 = const.LANG_ISO_639_1_TO_2_DICT[target_lang_iso_1]
    synsets = wn.synsets(word, pos=pos, lang=source_lang_iso_2)
    for synset in synsets:
        translations.extend(wn.synset(synset).lemma_names(target_lang_iso_2))
    return translations
