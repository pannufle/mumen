#! /usr/bin/python3
"""WordNet Translator.

Module to translate both words using wordnet.
"""
from collections import defaultdict
from nltk.corpus import wordnet as wn
from mumen.translation.dictionaries.base_dict import BaseDict


class WordNetDict(BaseDict):
    """WordNet based dictionary."""

    def __init__(self, source_lang, target_lang):
        """Initialize WordNet dictionary."""
        BaseDict.__init__(source_lang, target_lang)

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
        lemmas = defaultdict(lambda: 1)
        total = 0
        for syn in syns:
            for lemma in syn.lemma_names(self.__target__):
                lemmas[lemma] += 1
                total += 1
        if not total:
            return {}
        for lemma in lemmas:
            lemmas[lemma] /= total
        return lemmas
