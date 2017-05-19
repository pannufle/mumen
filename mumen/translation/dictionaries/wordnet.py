"""WordNet Translator.

Module to translate both words using wordnet.
"""
import logging

from nltk.corpus import wordnet as wn
import mumen.utils.constants as const

__all__ = ['get_translations']

logger = logging.getLogger(__name__)


def get_translations(lemma, target_lang_iso_1, config):
    """Get WordNet translations of word (with pos) from source to target
    language"""
    logger.debug('Loading WordNet dictionary')
    logger.debug('Translating entry: {}'.format(lemma))
    translations = []
    partition = lemma.rpartition(const.HYPHEN)
    word = partition[0]
    pos = partition[2]
    # TODO: Add validation for languages
    source_lang_iso_2 = const.LANG_ISO_639_1_TO_2_DICT[config['from']]
    target_lang_iso_2 = const.LANG_ISO_639_1_TO_2_DICT[target_lang_iso_1]
    synsets = wn.synsets(word, pos=const.MEN2WN_POS[pos], lang=source_lang_iso_2)
    if synsets:
        logger.debug('Corresponding synsets: {}'.format(synsets))
    else:
        logger.debug('No corresponding synsets found')
    for synset in synsets:
        wn_target_lemmas = synset.lemma_names(target_lang_iso_2)
        if wn_target_lemmas:
            logger.debug('Corresponding target lemmas: {}'.format(wn_target_lemmas))
        else:
            logger.debug('No corresponding target lemmas found')
        translations.extend(wn_target_lemmas)
    return ['{}-{}'.format(item, pos) for item in translations]
