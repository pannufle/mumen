#! /usr/bin/python3
"""Simple wrapper for JMDict."""
from collections import defaultdict
from lxml import etree
from mumen.translation.dictionaries.base_dict import BaseDict


class JMDict(BaseDict):
    """Load JMdict dictionaries and use it to translate words."""

    def __init__(self, file_path, source_lang, target_lang):
        """Initialize JMDict dictionary.

        Japanese and English are the only supported source/target
        languages for now.
        """
        BaseDict.__init__(self, source_lang, target_lang)
        self.__tree__ = etree.parse(file_path)

    def translate(self, word):
        """Translate word."""
        translations = defaultdict(lambda: 0)
        if self.source() == "eng":
            trans = self.__tree__.xpath('.//gloss[text()="{}"]'.format(word))
            for gloss in trans:
                froms = gloss.getparent().getparent().find(".//reb").text
                translations[froms] += 1
        else:
            trans = self.__tree__.xpath('.//keb[text()="{}"]'.format(word))
            for keb in trans:
                froms = keb.getparent().getparent().xpath(".//gloss")
                for trans in froms:
                    translations[trans.text] += 1
            trans = self.__tree__.xpath('.//reb[text()="{}"]'.format(word))
            for reb in trans:
                froms = reb.getparent().getparent().xpath(".//gloss")
                for trans in froms:
                    translations[trans.text] += 1
        return translations


if __name__ == "__main__":
    PATH = "../../../data/jmdict/dicts/JMdict_e"
    DICT = JMDict(PATH, "eng", "jpn")
    print(DICT.translate("house"))
