"""Here you will find all the constants used by MuMen."""

TEXT_FILE_EXTENSION = '.txt'
XML_FILE_EXTENSION = '.xml'

NEW_LINE = '\n'  # replace by os.linesep?
TAB = '\t'
WSPACE = ' '

HYPHEN = '-'

REGEX = {
    'whitespace': r'\s+'
}

JM2MEN_POS = {
    'noun (common) (futsuumeishi)': 'n',
    'adverbial noun (fukushitekimeishi)': 'n',
    'noun, used as a prefix': 'n',
    'noun, used as a suffix': 'n',
    'noun (temporal) (jisoumeishi)': 'n',
    'Ichidan verb': 'v',
    'Nidan verb with \'u\' ending (archaic)': 'v',
    'Yodan verb with `hu/fu\' ending (archaic)': 'v',
    'Yodan verb with `ru\' ending (archaic)': 'v',
    'Godan verb (not completely classified)': 'v',
    'Godan verb - -aru special class': 'v',
    'Godan verb with `bu\' ending': 'v',
    'Godan verb with `gu\' ending': 'v',
    'Godan verb with `ku\' ending': 'v',
    'Godan verb - iku/yuku special class': 'v',
    'Godan verb with `mu\' ending': 'v',
    'Godan verb with `nu\' ending': 'v',
    'Godan verb with `ru\' ending': 'v',
    'Godan verb with `ru\' ending (irregular verb)': 'v',
    'Godan verb with `su\' ending': 'v',
    'Godan verb with `tsu\' ending': 'v',
    'Godan verb with `u\' ending': 'v',
    'Godan verb with `u\' ending (special class)': 'v',
    'Godan verb - uru old class verb (old form of Eru)': 'v',
    'Godan verb with `zu\' ending': 'v',
    'Ichidan verb - zuru verb - (alternative form of -jiru verbs)': 'v',
    'intransitive verb': 'v',
    'kuru verb - special class': 'v',
    'irregular nu verb': 'v',
    'noun or participle which takes the aux. verb suru': 'v',
    'su verb - precursor to the modern suru': 'v',
    'suru verb - irregular': 'v',
    'suru verb - special class': 'v',
    'transitive verb': 'v',
    'adjective (keiyoushi)': 'j',
    'adjectival nouns or quasi-adjectives (keiyodoshi)': 'j',
    'nouns which may take the genitive case particle `no\'': 'j',
    'pre-noun adjectival (rentaishi)': 'j',
    '`taru\' adjective': 'j',
    'noun or verb acting prenominally (other than the above)': 'j',
    'former adjective classification (being removed)': 'j'
}

MEN2JM_POS = {
    'n': ['noun (common) (futsuumeishi)',
          'adverbial noun (fukushitekimeishi)',
          'noun, used as a prefix',
          'noun, used as a suffix',
          'noun (temporal) (jisoumeishi)'],
    'v': ['Ichidan verb',
          'Nidan verb with \'u\' ending (archaic)',
          'Yodan verb with `hu/fu\' ending (archaic)',
          'Yodan verb with `ru\' ending (archaic)',
          'Godan verb (not completely classified)',
          'Godan verb - -aru special class',
          'Godan verb with `bu\' ending',
          'Godan verb with `gu\' ending',
          'Godan verb with `ku\' ending',
          'Godan verb - iku/yuku special class',
          'Godan verb with `mu\' ending',
          'Godan verb with `nu\' ending',
          'Godan verb with `ru\' ending',
          'Godan verb with `ru\' ending (irregular verb)',
          'Godan verb with `su\' ending',
          'Godan verb with `tsu\' ending',
          'Godan verb with `u\' ending',
          'Godan verb with `u\' ending (special class)',
          'Godan verb - uru old class verb (old form of Eru)',
          'Godan verb with `zu\' ending',
          'Ichidan verb - zuru verb - (alternative form of -jiru verbs)',
          'intransitive verb',
          'kuru verb - special class',
          'irregular nu verb',
          'noun or participle which takes the aux. verb suru',
          'su verb - precursor to the modern suru',
          'suru verb - irregular',
          'suru verb - special class',
          'transitive verb'],
    'j': ['adjective (keiyoushi)',
          'adjectival nouns or quasi-adjectives (keiyodoshi)',
          'nouns which may take the genitive case particle `no\'',
          'pre-noun adjectival (rentaishi)',
          '`taru\' adjective',
          'noun or verb acting prenominally (other than the above)',
          'former adjective classification (being removed)']
}

_MEN2JM_POS = {
    'n': ['n', 'n-adv', 'n-pref', 'n-suf', 'n-t'],
    'v': ['v1', 'v2a-s', 'v4h', 'v4r', 'v5', 'v5aru', 'v5b', 'v5g', 'v5k', 'v5k-s', 'v5m', 'v5n', 'v5r', 'v5r-i', 'v5s', 'v5t', 'v5u', 'v5u-s', 'v5uru', 'v5z', 'vz', 'vi', 'vk', 'vn', 'vs', 'vs-c', 'vs-i', 'vs-s', 'vt'],
    'j': ['adj-i', 'adj-na', 'adj-no', 'adj-pn', 'adj-t', 'adj-f', 'adj']
}

MEN2WN_POS = {
    'n': ['n'],
    'v': ['v'],
    'j': ['a', 's'],
}

WN2MEN_POS = {
    'n': 'n',
    'v': 'v',
    'a': 'j',
    's': 'j'
}

ENGLISH_ISO_1 = 'en'

LANG_ISO_639_1_TO_2_DICT = {
    'ar': 'ara',
    'en': 'eng',
    'ja': 'jpn'
}

# ISO639-1 supported language codes
ISO639_1 = {
    'ar': 'Arabic',
    'en': 'English',
    'ja': 'Japanese'
}

# UTF-8 sentence separators by language ISO639-1 code
SENTENCE_SEPARATORS = {
    'ar': '\u06D4\u0021\u01C3\u061F',  # .!؟
    'en': '\u002E\u0021\u01C3\u003F\u203C\u2048\u2049',  # .!?
    'ja': '\u3002\uFF01\uFF1F'  # 。！？
}
