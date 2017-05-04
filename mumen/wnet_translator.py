#! /usr/bin/python3
"""WordNet Translator.

Module to translate both words and MEN entries.
"""
from nltk.corpus import wordnet as wn


def translate_word(word, lng="jpn"):
    """Function to translate an English word using WordNet.

    Args:
        word: English word to translate
        lng: target language
    Returns:
        Translated word
    """
    syns = wn.synsets(word)
    if len(syns) == 0:
        raise Exception("No synset found for {}".format(word))
    lemmas = set()
    for syn in syns:
        lemmas |= set(syn.lemma_names(lng))
    if len(lemmas) == 0:
        raise Exception("No translation found for {} in {}".format(word, lng))
    return lemmas


if __name__ == "__main__":
    print(translate_word("cat"))
    print(translate_word("dog"))
    print(translate_word("sun"))
    print(translate_word("japan"))
