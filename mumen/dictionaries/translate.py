#! /usr/bin/python3
"""Module to translate a MEN file.

author: Martino Ferrari
author_email: martino.ferrari@etu.unige.ch
"""
import mumen.dictionaries.wnet_dict as wnet
from mumen.constants import DICTIONARIES, Dictionary


def translate(men_pairs, config):
    """Translate MEN file pipeline.

    This function permits to use one dictionary to translate a MEN file.

    Args:
        men_pairs: MEN File parsed.
        config: YML config validated.

    Returns:
        translated MEN file.

    """
    module = config['Translation']
    if DICTIONARIES[module['dictionary']] == Dictionary.WORDNET:
        return wnet.translate_men(men_pairs, wnet.lang2str(module['language']))
    else:
        # TODO Implement other dictionaries!
        raise Exception("Other Dictionaries must be implemented")
