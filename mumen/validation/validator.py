#! /usr/bin/python3
"""Configuration Validator.

Load a yml mumen configuration and validate it.

author: Martino Ferrari
author_email: martino.ferrari@etu.unige.ch
"""
import yaml
from mumen.exceptions.validation import ValidationException
import mumen.validation.validators.men_extraction as men_extractor
import mumen.validation.validators.men_translation as men_translation


def load_yml(path):
    """Load a yml file using pyyaml library.

    Args:
        path: path to the file to load.

    Returns:
        the yml data structure.

    """
    with open(path, "r") as stream:
        try:
            return yaml.load(stream)
        except yaml.YAMLError as exc:
            raise ValidationException(exc)


def validate_yml(config):
    """Validate yml Configuration.

    Read and yml file, check the settings and return a valid configuration.

    Args:
        config: yml data structure.

    Returns:
        the validated yml data structure.

    """
    try:
        if config['MEN']:
            men_extractor.validate(config['MEN'])
        if config["Translation"]:
            men_translation.validate(config['Translation'])
    except KeyError as exc:
        raise ValidationException("Validation error: {}".format(exc))
    return config


if __name__ == "__main__":
    print(validate_yml(load_yml("../config/config.yml")))
