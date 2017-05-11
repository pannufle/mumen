#! /usr/bin/python3
"""Mumen main script.

Mumen read and translate MEN files and then use it to generate YACAB questions.

author: Martino Ferrari
author_email: martino.ferrari@etu.unige.ch
"""
import sys
import argparse
import logging
from mumen.validation.validator import validate_yml
from mumen.utils.men import men_pipeline
from mumen.utils.configloader import load_yml
from mumen.translation.translator import translate
from mumen.exceptions.translation import TranslationException
from mumen.exceptions.validation import ValidationException


def main():
    """Exec mumen.

    This is the main entry point of the project.
    """
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

        for men in translate(men_pipeline(config), config):
            logger.info(men)
    except (ValidationException, TranslationException) as exc:
        logger.error(exc)


if __name__ == "__main__":
    main()
