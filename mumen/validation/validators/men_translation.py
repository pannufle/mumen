#! /usr/bin/python3
"""Module to validate the Translation config section.

author: Martino Ferrari
author_email: martino.ferrari@etu.unige.ch
"""
from mumen.constants import LANGUAGES, DICTIONARIES
from mumen.exceptions.validation import ValidationException


def __validate_language__(lang):
    if lang not in LANGUAGES:
        raise ValidationException("Language not supported: {}".format(lang))


def __validate_dictionary__(dictionary):
    if dictionary not in DICTIONARIES:
        raise ValidationException("Dictionary not supported: {}".format(
            dictionary))


def validate(module):
    """Validate the Translation section.

    Args:
        module: Translation config section
    """
    if module['language']:
        __validate_language__(module['language'])
    else:
        raise ValidationException("No language defined in Translation.")
    if module['dictionary']:
        __validate_dictionary__(module['dictionary'])
    else:
        raise ValidationException("No dictionary specified for Translation.")
