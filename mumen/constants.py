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


class Lang(enum.Enum):
    """Languages enumerator.

    Simple enumarator for the mumen avaiable languages.
    """

    ENG = 0
    JPN = 1
    ARB = 2


class Dict(enum.Enum):
    """Dictionaries enumerator.

    Simple enumerator for the mumen avaiable dictionaries.
    """

    WORDNET = 0
    FREEDICT = 1
    JMDICT = 3
