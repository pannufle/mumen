#! /usr/bin/python3
"""Module to translate a MEN file.

author: Martino Ferrari
author_email: martino.ferrari@etu.unige.ch
"""
from mumen.constants import Dictionary
from mumen.translation.dictionaries.wnet_dict import WordNetDict
from mumen.exceptions.translation import TranslationException


class Translator:
    """Class to manage multilingual, multidictionaries translation"""
    def __init__(self, source_lang, target_lang, dictionaries):
        self.__source__ = source_lang
        self.__target__ = target_lang
        self.__dictionaries__ = []
        self.__load__dicts__(dictionaries)

    def __load__dicts__(self, dictionaries):
        for dic in dictionaries:
            if dic == Dictionary.WORDNET:
                self.__dictionaries__.append(WordNetDict(
                    self.__source__,
                    self.__target__))

    def translate(self, word):
        """Translate a single word."""
        translation = []
        for dic in self.__dictionaries__:
            translation.extend(dic.translate(word))
        if not translation:
            raise TranslationException(
                "No translation for the word: {}".format(word))
        return translation[0]

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

    Returns:
        translated MEN file.

    """
    translator = Translator(source_lang, target_lang, dictionaries)
    for (trad_a, trad_b, sim) in translator.translate_men_pairs(men_pairs):
        yield (trad_a, trad_b, sim)
