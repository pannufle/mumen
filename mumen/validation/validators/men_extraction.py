#! /usr/bin/python3
"""Module to validate the MEN config section.

author: Martino Ferrari
author_email: martino.ferrari@etu.unige.ch
"""


def validate_type(m_type):
    """Validate MEN type configuration."""
    return m_type == "natural" or m_type == "lemma"


def validate(config):
    """Validate MEN config section.

    Args:
        config: MEN config section
    """
    modules = {'type': False, 'source': False, 'language': False}
    for module in config:
        if module['type'] is True:
            modules['type'] = validate_type(module['type'])
    return modules['type'] and modules['source'] and modules['language']
