#! /usr/bin/python3
"""Mumen main script.

Mumen read and translate MEN files and then use it to generate YACAB questions.

author: Martino Ferrari
author_email: martino.ferrari@etu.unige.ch
"""
import sys
import logging
from mumen.constants import CONFIG_PATH
from mumen.validation.validator import load_yml, validate_yml
from mumen.men.men import men_pipeline
from mumen.dictionaries.translate import translate
from mumen.exceptions.translation import TException

if __name__ == "__main__":
    LOGGER = logging.getLogger("MUMEN")
    LOGGER.setLevel(logging.DEBUG)
    logging.basicConfig(stream=sys.stdout)

    CONFIG = validate_yml(load_yml(CONFIG_PATH))
    try:
        for men in translate(men_pipeline(CONFIG), CONFIG):
            LOGGER.info(men)
    except TException as exc:
        LOGGER.error(exc)
