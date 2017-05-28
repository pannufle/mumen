"""Simple wrapper for FreeDict."""
import logging
# import lxml.etree as etree
# import mumen.utils.constants as const

"""
TODO: Repair this wrapper
"""


# __all__ = ['get_translations']

logger = logging.getLogger(__name__)


# TEI namespaces
TEI_NS = {'n': 'http://www.tei-c.org/ns/1.0'}


"""def _load(dictionary_path, source_lang, target_lang):
    # Initialize FreeDict dictionary.
    __tree__ = etree.parse(dictionary_path)
    __direct__ = '{}-{}'.format(
        source_lang.to_3_lang_id(),
        target_lang.to_3_lang_id()) in dictionary_path


def get_translations(word, pos, target_lang_iso_1, config):
    # Translate a given entry using FreeDict.
    translations = []
    total = 0
    if not __direct__:
        query = '..//n:entry[.//n:quote[text()="{}"]]'.format(word)
        sub_query = './/n:orth'
    else:
        query = '..//n:entry[.//n:orth[text()="{}"]]'.format(word)
        sub_query = './/n:quote'
    trans = __tree__.xpath(query, namespaces=TEI_NS)
    for entry in trans:
        froms = entry.xpath(sub_query, namespaces=TEI_NS)
        for trans in froms:
            translations[trans.text] += 1
            total += 1
    for tran in translations:
        translations[tran] /= total
    return translations
"""
