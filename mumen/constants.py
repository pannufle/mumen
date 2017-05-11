#! /usr/bin/python3
"""Mumen constants.

Few constants and enum for the mumen project.
"""
import enum


class MENType(enum.Enum):
    """MEN Type enumarator.

    Simple enumerator for the MEN file type.
    """

    NATURAL = 0
    LEMMA = 1

    @staticmethod
    def convert(string):
        """Convert string to MENType.

        Args
        ----
            string: string to convert.

        Returns
        -------
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

    English = 0
    Japanese = 1
    Arabic = 2

    @staticmethod
    def from_lang_id(lang_id):
        """Convert letter identifier into Lang enum."""
        if lang_id == "en":
            return Lang.English
        if lang_id == "ja":
            return Lang.Japanese
        if lang_id == "ar":
            return Lang.Arabic

    def to_lang_id(self):
        """Convert Lang enum to 2 letter identifier."""
        if self == Lang.English:
            return "en"
        if self == Lang.Japanese:
            return "ja"
        if self == Lang.Arabic:
            return "ar"

    def to_3_lang_id(self):
        """Convert Lang enum to 3 letter identifier."""
        if self == Lang.English:
            return "eng"
        if self == Lang.Japanese:
            return "jpn"
        if self == Lang.Arabic:
            return "ara"

    def to_wnet_lang_id(self):
        """Convert Lang enum to wordnet letter identifier."""
        if self == Lang.English:
            return "eng"
        if self == Lang.Japanese:
            return "jpn"
        if self == Lang.Arabic:
            return "arb"


class Dictionary(enum.Enum):
    """Dictionaries enumerator.

    Simple enumerator for the mumen avaiable dictionaries.
    """

    WORDNET = 0
    FREEDICT = 1
    JMDICT = 3

    @staticmethod
    def from_name(name):
        """Convert name string to enum."""
        return DICTIONARIES[name]


DICTIONARIES = {"wordnet": Dictionary.WORDNET,
                "freedict": Dictionary.FREEDICT,
                "jmdict": Dictionary.JMDICT}

FREEDICT_DICTS = {
    "jpn-eng": "jpn-eng",
    "eng-jpn": "jpn-eng",
    "ara-eng": "ara-eng",
    "eng-ara": "eng-ara"
}
