#! /usr/bin/python3
"""WordNet Translator.

Module to translate both words and MEN entries.

author: Martino Ferrari
author_email: martino.ferrari@etu.unige.ch
"""
from nltk.corpus import wordnet as wn


class WordNetDict:
    """WordNet based dictionary."""
    def __init__(self, source_lang, target_lang):
        self.__source__ = source_lang.to_wnet_lang_id()
        self.__target__ = target_lang.to_wnet_lang_id()

    def source(self):
        """Get source language."""
        return self.__source__

    def target(self):
        """Get target language."""
        return self.__target__

    def translate(self, word):
        """Translate a word using WordNet.

        Args:
            word: word to translate
        Returns:
            Translated word

        """
        syns = wn.synsets(word)
        if not syns:
            return []
        lemmas = []
        for syn in syns:
            for lemma in syn.lemma_names(self.__target__):
                if lemma not in lemmas:
                    lemmas.append(lemma)
        return lemmas
