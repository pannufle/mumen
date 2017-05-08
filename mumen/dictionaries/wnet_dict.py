#! /usr/bin/python3
"""WordNet Translator.

Module to translate both words and MEN entries.

author: Martino Ferrari
author_email: martino.ferrari@etu.unige.ch
"""
from nltk.corpus import wordnet as wn
from mumen.exceptions.translation import TException


def translate_word(word, lng="jpn"):
    """Translate an English word using WordNet.

    Args:
        word: English word to translate
        lng: target language
    Returns:
        Translated word

    """
    syns = wn.synsets(word)
    if not syns:
        raise TException("No synset found for {}".format(word))
    lemmas = set()
    for syn in syns:
        lemmas |= set(syn.lemma_names(lng))
    if not lemmas:
        raise TException("No translation found for {} in {}".format(word, lng))
    return lemmas


if __name__ == "__main__":
    print(translate_word("cat"))
    print(translate_word("dog"))
    print(translate_word("sun"))
    print(translate_word("japan"))
