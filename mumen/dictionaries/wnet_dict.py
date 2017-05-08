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


def translate_men(men, lng="jpn"):
    """Translate a MEN dataset using WordNet.

    Args:
        men: An english MEN dataset to translate
        lng: target language
    Returns:
        Translated MEN dataset in target language

    """
    translated_men = []
    for entry in men:
        translated_men.append(
            translate_word(entry["word_L"], lng),
            translate_word(entry["word_R"], lng),
            entry["similarity"])
    return translate_men


if __name__ == "__main__":
    print(translate_word("cat"))
    print(translate_word("dog"))
    print(translate_word("sun"))
    print(translate_word("japan"))
