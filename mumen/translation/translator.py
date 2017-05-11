#! /usr/bin/python3
"""Module to translate a MEN file."""
import operator
import logging
from collections import defaultdict
from mumen.exceptions.translation import TranslationException


class Translator:
    """Class to manage multilingual, multidictionaries translation."""

    def __init__(self, source_lang, target_lang, dictionaries):
        """Initialize translator."""
        self.__source__ = source_lang
        self.__target__ = target_lang
        self.__dictionaries__ = dictionaries

    def translate(self, word):
        """Translate a single word."""
        translation = defaultdict(int)
        for dic in self.__dictionaries__:
            translated = dic.translate(word)
            for trans in translated:
                translation[trans] += translated[trans]
        if not translation:
            raise TranslationException(
                "No translation for the word: {}".format(word))
        sorted_trans = sorted(translation.items(),
                              key=operator.itemgetter(1),
                              reverse=True)
        return sorted_trans[0][0]

    def translate_pairs(self, word_a, word_b):
        """Translate couple of words."""
        return self.translate(word_a), self.translate(word_b)

    def translate_men_pairs(self, men_pairs):
        """Translate a list of couples of words."""
        for (word_a, word_b, sim) in men_pairs:
            trans_a, trans_b = self.translate_pairs(word_a, word_b)
            yield (trans_a, trans_b, sim)


def translate(men_pairs, source_lang, target_lang, dictionaries):
    """Translate MEN file pipeline.

    This function permits to use one dictionary to translate a MEN file.

    Args:
        men_pairs: MEN File parsed.
        source_lang: original lang
        target_lang: target lang
        dictionaries: list of enabled dictionaries

    Returns
    -------
        translated MEN file.

    """
    logger = logging.getLogger(__name__)
    translator = Translator(source_lang, target_lang, dictionaries)

    for (word_a, word_b, sim) in men_pairs:
        try:
            trad_a, trad_b = translator.translate_pairs(word_a, word_b)
            yield (trad_a, trad_b, sim)
        except TranslationException as exc:
            logger.warning(exc)
