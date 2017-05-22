"""Simple wrapper for JMDict."""
import logging
from functools import lru_cache
from collections import defaultdict
import xml.etree.ElementTree as element_tree
import mumen.utils.constants as const
from mumen.exceptions.parameter import InvalidParameterError


__all__ = ['get_translations']

logger = logging.getLogger(__name__)


def _extract_english_tokens(entry):
    tokens = set()
    for sense in entry.findall('sense'):
        glosses = sense.findall('gloss')
        for gloss in glosses:
            # If it is the English gloss
            if gloss.get(
                    '{http://www.w3.org/XML/1998/namespace}lang') == 'eng':
                tokens.add(gloss.text)
    return tokens


def _extract_japanese_tokens(entry):
    """The k_ele stands for the kanji-based element.
    r_ele is the reading (in furigana).
    If the word is written in furigana,
    r_ele is the defining element. Otherwise it is k_ele
    """
    tokens = set()
    k_eles = entry.findall('k_ele')
    if not k_eles:
        for r_ele in entry.findall('r_ele'):
            reb = r_ele.find('reb')  # There is always only one reb
            tokens.add(reb.text)
    else:
        for k_ele in k_eles:
            keb = k_ele.find('keb')  # There is always only one keb.
            tokens.add(keb.text)
    return tokens


def _extract_pos_tags(entry):
    pos_tags = set()
    for sense in entry.findall('sense'):
        _pos_tags = sense.findall('pos')
        for _pos_tag in _pos_tags:
            pos_tags.add(_pos_tag.text)
    return pos_tags


def _load_en_ja_dict(path):
    jmdict = defaultdict(set)
    tree = element_tree.parse(path)
    root = tree.getroot()
    for entry in root.findall('entry'):
        ja_tokens = _extract_japanese_tokens(entry)
        en_tokens = _extract_english_tokens(entry)
        pos_tags = _extract_pos_tags(entry)
        for en_token in en_tokens:
            for ja_token in ja_tokens:
                for pos_tag in pos_tags:
                    jmdict[(en_token, pos_tag)].add((ja_token, pos_tag))
    return jmdict


@lru_cache(maxsize=None)
def _load(source_lang_iso_1, target_lang_iso_1, path):
    if source_lang_iso_1 == 'en' and target_lang_iso_1 == 'ja':
        # Currently only supporting English to Japanese dictionary
        return _load_en_ja_dict(path)
    else:
        raise InvalidParameterError('Unsupported configuration with source\
        language \'{}\' and target language \'{}\'. Cannot load JMDict'
                                    .format(source_lang_iso_1,
                                            target_lang_iso_1))


def get_translations(lemma, target_lang_iso_1, config):
    """Translate a given entry using JMDict."""
    logger.debug('Loading JMDict...')
    jmdict = _load(config['from'], target_lang_iso_1,
                   config['dictionaries']['jmdict']['path'])
    logger.debug('JMDict loaded')
    partition = lemma.rpartition(const.HYPHEN)
    word = partition[0]
    pos = partition[2]
    logger.debug('Converting {}-{} to JMDict entry...'.format(word, pos))
    # for key, value in jmdict.items():
    # print('Key = {} Value = {}'.format(key, value))
    jmd_lemmas = {(word, jmdict_pos) for jmdict_pos in const.MEN2JM_POS[pos]}
    # logger.debug('  JMDict entries: {}'.format(lemmas))
    translations = set()
    for jmd_lemma in jmd_lemmas:
        for translation in jmdict[jmd_lemma]:
            translations.add(translation[0])
    return translations


if __name__ == '__main__':
    logging.basicConfig(format='%(levelname)s - %(message)s',
                        level=logging.DEBUG)
    __config__ = {
        'from': 'en',
        'dictionaries': {
            'jmdict': {
                'use': True,
                'path':
                '/Users/AKB/GitHub/mumen/data/dictionaries/jmdict/jmdict.xml'
            }
        }
    }
    print(get_translations('scalar-n', 'ja', __config__))
    print(get_translations('sweatshirt-n', 'ja', __config__))
    print(get_translations('joint-n', 'ja', __config__))
