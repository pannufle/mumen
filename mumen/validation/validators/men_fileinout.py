#! /usr/bin/python3
"""Module to validate the MEN config section."""
from mumen.exceptions.validation import ValidationException


def validate(module):
    """
    Validate MEN config section.

    Args:
        module: MEN config section
    """
    if not module:
        raise ValidationException("No module found!")
