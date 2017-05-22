"""Validation module for MuMen.

Details
"""

import logging

import mumen.utils.constants as const
from mumen.exceptions.validation import ValidationError


logger = logging.getLogger(__name__)

__all__ = ['validate_config', 'validate_iso639_1_code']


def validate_iso639_1_code(lang_iso_code):
    """Validate language ISO639-1 code."""
    if len(lang_iso_code) != 2:
        raise ValidationError('Configuration filename should contain 2'
                              'characters referring to the parsed language'
                              'ISO639-1 code')
    if lang_iso_code not in const.ISO639_1:
        raise ValidationError('Unsupported language code: {}'.format(
            lang_iso_code))


def validate_config(config):
    """Validate config parameters."""
    try:
        logger.info('Validating config parameters...')
        if config['translate']:
            # translation.validate(config['translation'])
            pass
        if config['generate']:
            # generation.validate(config['generation'])
            pass
        if config['compute']:
            # computation.validate(config['computation'])
            pass
        logger.info('All config parameters are valid')
    except ValidationError:
        raise
