#! /usr/bin/python3
"""Mumen main script.

Mumen read and translate MEN files and then use it to generate YACAB surveys.
"""
import sys
import argparse
import logging
import yaml

import mumen.translation.translator as translator
import mumen.validation.validator as validator
import mumen.utils.files as futils
from mumen.exceptions.input import InvalidInputError
from mumen.exceptions.method import InvalidMethodError
from mumen.exceptions.parameter import InvalidParameterError
from mumen.exceptions.validation import ValidationError
from mumen.utils.immutables import ImmutableConfig




from mumen.constants import Lang, Dictionary, FREEDICT_DICTS
from mumen.translation.dictionaries.free_dict import FreeDict
from mumen.translation.dictionaries.wnet_dict import WordNetDict
from mumen.translation.dictionaries.jm_dict import JMDict

logging.basicConfig(format='%(levelname)s - %(message)s',
                    level=logging.DEBUG)
logger = logging.getLogger(__name__)


def __freedict_conf__(config, source_lang, target_lang):
    dict_path = config['freedict_conf']['dict_dir']
    basepath = '{}-{}'.format(source_lang.to_3_lang_id(),
                              target_lang.to_3_lang_id())
    basepath = FREEDICT_DICTS[basepath]
    dict_path = '{}{}/{}.tei'.format(dict_path, basepath, basepath)
    return dict_path


def __jmdict_conf__(config):
    dict_path = config['jmdict_conf']['dict_file']
    return dict_path


def __load_dicts__(config, source_lang, target_lang):
    dictionaries = []
    for entry in config['translator']:
        for name in entry:
            enabled = entry[name]
            if enabled:
                dic = Dictionary.from_name(name)
                if dic == Dictionary.WORDNET:
                    dictionaries.append(WordNetDict(source_lang, target_lang))
                elif dic == Dictionary.FREEDICT:
                    # freedic config
                    dict_path = __freedict_conf__(config, source_lang,
                                                  target_lang)
                    freedict = FreeDict(dict_path,
                                        source_lang,
                                        target_lang)
                    dictionaries.append(freedict)
                elif dic == Dictionary.JMDICT:
                    file_path = __jmdict_conf__(config)
                    jmdict = JMDict(file_path, source_lang, target_lang)
                    dictionaries.append(jmdict)
    return dictionaries


def __translation__(config):
    logger = logging.getLogger(__name__)
    # input MEN file
    in_file = config['source']['file']
    # source lang
    source_lang = Lang.from_lang_id(config['source']['lang'])
    # target lang
    target_lang = Lang.from_lang_id(config['target']['lang'])
    # load dictionaries
    dictionaries = __load_dicts__(config, source_lang, target_lang)
    # start translation process
    for translation in translator.translate(
            men.load(in_file),
            source_lang,
            target_lang,
            dictionaries):
        logger.info(translation)


def main():
    """Launch the MuMen application with the provided config file."""
    parser = argparse.ArgumentParser(
        description='Translate MEN and generate YACAB questions.')
    parser.add_argument(
        'config', metavar='config', type=str,
        help='YML configuration to load.')
    logger.info('Welcome to MuMEN!')
    args = parser.parse_args()
    config_file = args.config
    logger.info('Launching Nima with config: {}'.format(config_file))

    try:
        lang_iso_code = futils.get_filename(config_file)
        validator.validate_iso639_1_code(lang_iso_code)

        with open(config_file, 'r') as config_stream:
            config = yaml.safe_load(config_stream)
            iconfig = ImmutableConfig(config)
            if iconfig['translate']:
                translator.translate_dataset(lang_iso_code,
                                             iconfig['translation'])
    except (ValidationError, InvalidParameterError, InvalidMethodError,
            InvalidInputError) as err:
        logger.error(err)
        logger.error('Exiting MuMen')
        sys.exit(1)  # exit with error code 1 when program errors


if __name__ == "__main__":
    main()
