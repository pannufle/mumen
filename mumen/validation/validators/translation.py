#! /usr/bin/python3
"""Module to validate the Translation config section.

author: Martino Ferrari
author_email: martino.ferrari@etu.unige.ch
"""
# from mumen.constants import DICTIONARIES
# from mumen.exceptions.validation import ValidationException
import mumen.validation.validators.men_fileinout as meninout


# def __validate_translator__(config):
#     for dic in DICTIONARIES:
#         if dic not in config:
#             raise ValidationException("No {} in configuration".format(dic))
#     return True


def validate(module):
    """Validate the Translation section.

    Args:
        module: Translation config section
    """
    meninout.validate(module['source'])
    meninout.validate(module['target'])
    # __validate_translator__(module['translator'])
