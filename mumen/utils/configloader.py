#! /usr/bin/python3
"""Utils to load and store yaml config file.

author: Martino Ferrari
author_email: martino.ferrari@etu.unige.ch
"""
import yaml
from mumen.exceptions.loading import ConfigException


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
            raise ConfigException(exc)
