"""Here you will find all the constants used by MuMen."""

TEXT_FILE_EXTENSION = '.txt'
XML_FILE_EXTENSION = '.xml'

NEW_LINE = '\n'  # replace by os.linesep?
TAB = '\t'
WSPACE = ' '

HYPHEN = '-'

MEN2WN_POS = {
    'n': 'n',
    'v': 'v',
    'j': 'a',
}

WN2MEN_POS = {
    'n': 'n',
    'v': 'v',
    'a': 'j'
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
