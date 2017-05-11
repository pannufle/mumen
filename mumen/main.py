#! /usr/bin/python3
"""
Mumen main script.

Mumen read and translate MEN files and then use it to generate YACAB questions.
"""
import sys
import argparse
import logging
from mumen.validation.validator import validate_yml
import mumen.utils.men as men
from mumen.utils.configloader import load_yml
from mumen.constants import Lang, Dictionary
from mumen.translation.translator import translate
from mumen.exceptions.translation import TranslationException
from mumen.exceptions.validation import ValidationException


def __translation__(config):
    logger = logging.getLogger(__name__)

    in_file = config['source']['file']
    # out_file = config['target']['file']
    source_lang = Lang.from_lang_id(config['source']['lang'])
    target_lang = Lang.from_lang_id(config['target']['lang'])
    dictionaries = []
    for entry in config['translator']:
        for name in entry:
            enabled = entry[name]
            if enabled:
                dictionaries.append(Dictionary.from_name(name))
    for translation in translate(
            men.load(in_file),
            source_lang,
            target_lang,
            dictionaries):
        logger.info(translation)


def main():
    """Launch the MuMen application with the provided config file."""
    logging.basicConfig(format='%(levelname)s - %(message)s',
                        level=logging.DEBUG,
                        stream=sys.stdout)
    parser = argparse.ArgumentParser(
        description='Translate MEN and generate YACAB qeustions.')
    parser.add_argument(
        'config', metavar='config', type=str,
        help='YML configuration to load.')
    logger = logging.getLogger(__name__)
    logger.info("Welcome to MuMEN!")
    args = parser.parse_args()
    config_file = args.config
    logger.info("Loading config: %s", config_file)
    try:
        logger.setLevel(logging.DEBUG)
        config = validate_yml(load_yml(config_file))
        if config['translation']:
            __translation__(config['translation_step'])
    except (ValidationException, TranslationException) as exc:
        logger.error(exc)


if __name__ == "__main__":
    main()
