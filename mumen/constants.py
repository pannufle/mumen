#! /usr/bin/python3
"""Mumen constants.

Few constants and enum for the mumen project.

author: Martino Ferrari
author_email: martino.ferrari@etu.unige.ch
"""
import enum


CONFIG_PATH = "mumen/config/config.yml"


class MENType(enum.Enum):
    """MEN Type enumarator.

    Simple enumerator for the MEN file type.
    """

    NATURAL = 0
    LEMMA = 1

    @staticmethod
    def convert(string):
        """Convert string to MENType.

        Args:
            string: string to convert.

        Returns:
            MENType enum.

        """
        if string == "natural":
            return MENType.NATURAL
        elif string == "lemma":
            return MENType.LEMMA
        else:
            raise Exception("String can not be converted: {}".format(string))


class Lang(enum.Enum):
    """Languages enumerator.

    Simple enumarator for the mumen avaiable languages.
    """

    ENG = 0
    JPN = 1
    ARB = 2


class Dictionary(enum.Enum):
    """Dictionaries enumerator.

    Simple enumerator for the mumen avaiable dictionaries.
    """

    WORDNET = 0
    FREEDICT = 1
    JMDICT = 3


ONLINE_SOURCE = "online"
LANGUAGES = {"Arabic": Lang.ARB, "English": Lang.ENG, "Japanese": Lang.JPN}
DICTIONARIES = {"WordNet": Dictionary.WORDNET,
                "FreeDict": Dictionary.FREEDICT,
                "JMDict": Dictionary.JMDICT}
