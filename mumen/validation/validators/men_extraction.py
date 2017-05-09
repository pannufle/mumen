#! /usr/bin/python3
"""Module to validate the MEN config section.

author: Martino Ferrari
author_email: martino.ferrari@etu.unige.ch
"""
import os.path
from mumen.constants import LANGUAGES, ONLINE_SOURCE
from mumen.exceptions.validation import ValidationException


def __validate_type__(m_type):
    if not (m_type == "natural" or m_type == "lemma"):
        raise ValidationException("MEN Type value wrong: {}".format(m_type))
    return True


def __validate_source__(m_source):
    if not m_source == ONLINE_SOURCE:
        if m_source.startswith("path:"):
            path = m_source.split('path:')[1]
            if os.path.isfile(path):
                return True
        raise ValidationException("MEN source not valid: {}".format(m_source))
    return True


def __validate_language__(m_language):
    if m_language not in LANGUAGES:
        raise ValidationException("Language not supported: {}".format(
            m_language))
    return True


def validate(module):
    """Validate MEN config section.

    Args:
        module: MEN config section
    """
    modules = {'type': False, 'source': False, 'language': False}
    if 'type' in module:
        modules['type'] = __validate_type__(module['type'])
    if 'source' in module:
        modules['source'] = __validate_source__(module['source'])
    if 'language' in module:
        modules['language'] = __validate_language__(module['language'])
    if not (modules['type'] and modules['source'] and modules['language']):
        raise ValidationException("Missing part of MEN configuration.")
