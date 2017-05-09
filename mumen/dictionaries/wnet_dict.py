#! /usr/bin/python3
"""WordNet Translator.

Module to translate both words and MEN entries.

author: Martino Ferrari
author_email: martino.ferrari@etu.unige.ch
"""
from nltk.corpus import wordnet as wn
from mumen.constants import Lang, LANGUAGES
from mumen.exceptions.translation import TException


def lang2str(lang):
    """Convert Lang enum to wnet string.

    Args:
        lang: Lang enum.

    Returns:
        wordnet language string.

    """
    if isinstance(lang, str):
        lang = LANGUAGES[lang]
    if lang == Lang.JPN:
        return "jpn"
    if lang == Lang.ENG:
        return "eng"
    if lang == Lang.ARB:
        return "arb"
    raise Exception("Lang not supported: {}".format(lang))


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
    lemmas = []
    for syn in syns:
        lemmas.extend(syn.lemma_names(lng))
    if not lemmas:
        raise TException("No translation found for {} in {}".format(word, lng))
    return lemmas[0]


def translate_men(men, lng="jpn"):
    """Translate a MEN dataset using WordNet.

    Args:
        men: An english MEN dataset to translate
        lng: target language
    Returns:
        Translated MEN dataset in target language

    """
    for entry in men:
        yield {
            "word_L": translate_word(entry["word_L"], lng),
            "word_R": translate_word(entry["word_R"], lng),
            "similarity": entry["similarity"]
        }


if __name__ == "__main__":
    print(translate_word("cat"))
    print(translate_word("dog"))
    print(translate_word("sun"))
    print(translate_word("japan"))
