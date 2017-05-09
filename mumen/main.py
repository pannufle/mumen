#! /usr/bin/python3
"""Mumen main script.

Mumen read and translate MEN files and then use it to generate YACAB questions.

author: Martino Ferrari
author_email: martino.ferrari@etu.unige.ch
"""
import sys
import argparse
import logging
from mumen.validation.validator import load_yml, validate_yml
from mumen.men.men import men_pipeline
from mumen.dictionaries.translate import translate
from mumen.exceptions.translation import TException
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
        'conf_path', metavar='conf_path', type=str,
        help='YML configuration to load.')
    logger = logging.getLogger(__name__)
    logger.info("Welcome to MuMEN!")
    args = parser.parse_args()
    conf_path = args.conf_path
    logger.info("Loading config: %s", conf_path)
    try:
        logger.setLevel(logging.DEBUG)
        config = validate_yml(load_yml(conf_path))

        for men in translate(men_pipeline(config), config):
            logger.info(men)
    except (ValidationException, TException) as exc:
        logger.error(exc)


if __name__ == "__main__":
    main()
