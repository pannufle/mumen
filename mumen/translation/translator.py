#! /usr/bin/python3
"""Module to translate a MEN file.

author: Martino Ferrari
author_email: martino.ferrari@etu.unige.ch
"""


class Translator:
    """Class to manage multilingual, multidictionaries translation"""
    def __init__(self, source_lang, target_lang, dictionaries):
        self.__source__ = source_lang
        self.__target__ = target_lang
        self.__dictionaries__ = dictionaries

    def translate(self, word):
        """Translate a single word."""
        return word

    def translate_pairs(self, word_a, word_b):
        """Translate couple of words."""
        return self.translate(word_a), self.translate(word_b)

    def translate_men_pairs(self, men_pairs):
        """Translate a list of couples of words."""
        for (word_a, word_b) in men_pairs:
            yield self.translate_pairs(word_a, word_b)


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
    for (trad_a, trad_b) in translator.translate_men_pairs(men_pairs):
        yield (trad_a, trad_b)
