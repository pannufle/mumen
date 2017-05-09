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

if __name__ == "__main__":
    LOGGER = logging.getLogger("MUMEN")
    LOGGER.setLevel(logging.DEBUG)
    logging.basicConfig(stream=sys.stdout)

    for men in men_pipeline(validate_yml(load_yml(CONFIG_PATH))):
        LOGGER.info(men)
