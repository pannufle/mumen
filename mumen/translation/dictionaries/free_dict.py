#! /usr/bin/python3
"""Simple wrapper for FreeDict."""
from collections import defaultdict
from lxml import etree

# TEI namespaces
TEI_NS = {'n': 'http://www.tei-c.org/ns/1.0'}


class FreeDict:
    """Load freedict dictionaries and use it to translate words."""
    
    def __init__(self, dictionary_path, source_lang, target_lang):
        self.__tree__ = etree.parse(dictionary_path)
        self.__target__ = target_lang
        self.__source__ = source_lang
        self.__direct__ = '{}-{}'.format(
            source_lang, target_lang) in dictionary_path

    def source(self):
        """Get source language."""
        return self.__source__

    def target(self):
        """Get target language."""
        return self.__target__

    def translate(self, word):
        """Translate word."""
        translations = defaultdict(lambda: 0)
        total = 0
        if not self.__direct__:
            trans = self.__tree__.xpath(
                '..//n:entry[.//n:quote[text()="{}"]]'.format(word),
                namespaces=TEI_NS)
            for entry in trans:
                froms = entry.xpath('.//n:orth', namespaces=TEI_NS)
                for trans in froms:
                    translations[trans.text] += 1
                    total += 1
        else:
            trans = self.__tree__.xpath(
                '..//n:entry[.//n:orth[text()="{}"]]'.format(word),
                namespaces=TEI_NS)
            for entry in trans:
                froms = entry.xpath('.//n:quote', namespaces=TEI_NS)
                for trans in froms:
                    translations[trans.text] += 1
                    total += 1
        for tran in translations:
            translations[tran] /= total
        return translations


if __name__ == "__main__":
    PATH = "../../../data/freedict/dicts/jpn-eng/jpn-eng.tei"
    DICT = FreeDict(PATH, "eng", "jpn")
    print(DICT.translate("house"))
