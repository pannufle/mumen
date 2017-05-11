#! /usr/bin/python3
"""MEN Utilities.

This module contains many utilities to load, creante and store MEN Files:
https://staff.fnwi.uva.nl/e.bruni/MEN.

author: Martino Ferrari
author_email: martino.ferrari@etu.unige.ch
"""


def parse_men_row(row):
    """Parse a MEN row.

    Args:
        row: input row in form of "WORD_L WORD_R SIMILARITY"
    Returns:
        a dictionary in the form of:
        {
            "word_L": str,
            "word_R": str,
            "similarity": float
        }

    """
    men_row = row.strip().split()
    return {
        "word_L": men_row[0],
        "word_R": men_row[1],
        "similarity": float(men_row[2])
    }


def encode_men_row(entry):
    """Encode an MEN entry to .

    Args:
        entry: MEN entry in form of dictionary
    Returns:
        MEN entry string

    """
    return '{} {} {}'.format(entry["word_L"],
                             entry["word_R"],
                             entry["similarity"])


def load(path):
    """Load a MEN FILE.

    Args:
        path: path to the MEN file to load.

    Returns:
        the MEN Structure.

    """
    with open(path, "r") as men_file:
        for men_row in men_file:
            yield parse_men_row(men_row)


def store(men, path):
    """Store a MEN list to file.

    Args:
        param men: men list structure to save.
        param path: path to the file where to store the MEN.
    """
    with open(path, "w") as men_file:
        for entry in men:
            men_file.write('{}\n'.format(encode_men_row(entry)))


def men_pipeline(config):
    """Exec MEN pipeline.

    Args:
        config: YML validate config.

    Returns:
        pairs of MEN words.

    """
    module = config['MEN']

    path = module['source']
    return load(path)
