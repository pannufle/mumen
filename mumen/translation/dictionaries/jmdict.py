"""Simple wrapper for JMDict."""
import logging
import lxml.etree as etree
import mumen.utils.constants as const


__all__ = ['get_translations']

logger = logging.getLogger(__name__)

__tree__ = None


def get_translations(word, pos, target_lang_iso_1, config):
    """Translate a given entry using JMDict."""
    # TODO: include the part of speech
    translations = []
    if __tree__ is None:
        __tree__ = etree.parse(config['path'])
    if config['from'] == const.ENGLISH_ISO_1:
        trans = __tree__.xpath('.//gloss[text()="{}"]'.format(word))
        for gloss in trans:
            forms = gloss.getparent().getparent().find(".//reb").text
            translations.extend(forms)
    else:
        trans = __tree__.xpath('.//keb[text()="{}"]'.format(word))
        for keb in trans:
            forms = keb.getparent().getparent().xpath(".//gloss")
            for trans in forms:
                translations.extend(trans.text)
        trans = __tree__.xpath('.//reb[text()="{}"]'.format(word))
        for reb in trans:
            forms = reb.getparent().getparent().xpath(".//gloss")
            for trans in forms:
                translations.extend(trans.text)
    return translations
