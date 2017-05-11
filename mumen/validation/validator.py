#! /usr/bin/python3
"""
Configuration Validator.

Load a yml mumen configuration and validate it.
"""
from mumen.exceptions.validation import ValidationException
import mumen.validation.validators.translation as translation
import mumen.validation.validators.generation as generation
import mumen.validation.validators.computation as computation


def validate_yml(config):
    """
    Validate yml Configuration.

    Read and yml file, check the settings and return a valid configuration.

    Args:
        config: yml data structure.

    Returns
    -------
        the validated yml data structure.

    """
    try:
        if config['translation']:
            translation.validate(config['translation_step'])
        if config['generation']:
            generation.validate(config['generation_step'])
        if config['computation']:
            computation.validate(config['computation_step'])
    except KeyError as exc:
        raise ValidationException("Validation error: {}".format(exc))
    return config
