#! /usr/bin/python3
"""Mumen main script.

Mumen read and translate MEN files and then use it to generate YACAB questions.

author: Martino Ferrari
author_email: martino.ferrari@etu.unige.ch
"""
from mumen.constants import CONFIG_PATH
from mumen.validation.validator import load_yml, validate_yml

if __name__ == "__main__":
    # TODO implement pipeline
    validate_yml(load_yml(CONFIG_PATH))
