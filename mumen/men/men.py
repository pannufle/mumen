#! /usr/bin/python3
"""MEN Utilities.

This module contains many utilities to load, creante and store MEN Files:
https://staff.fnwi.uva.nl/e.bruni/MEN.

author: Martino Ferrari
author_email: martino.ferrari@etu.unige.ch
"""
import os
import zipfile
import requests
from mumen.constants import ONLINE_SOURCE, MENType


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


def downlaod_men(m_type):
    """Download the last version of the MEN data-set.

    Base url:  https://staff.fnwi.uva.nl/e.bruni/resources.

    Returns:
        The MEN structure

    """
    reponse = requests.get(
        "https://staff.fnwi.uva.nl/e.bruni/resources/MEN.zip",
        stream=True)
    if reponse.status_code == 200:
        if not os.path.isdir(".tmp/"):
            os.mkdir(".tmp")
        if not os.path.isdir(".tmp/MEN/"):
            with open(".tmp/MEN.zip", 'wb') as download:
                for chunk in reponse:
                    download.write(chunk)
            with zipfile.ZipFile(".tmp/MEN.zip", "r") as zip_ref:
                zip_ref.extractall(".tmp/")
        if m_type == MENType.NATURAL:
            return load(".tmp/MEN/MEN_dataset_natural_form_full")
        return load(".tmp/MEN/MEN_dataset_lemma_form_full")
    else:
        raise Exception("Download failed ({}) : {}".format(reponse.status_code,
                                                           reponse.text))


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
    if module['source'] == ONLINE_SOURCE:
        return downlaod_men(MENType.convert(module['type']))

    path = module['source'].split('path:')[1]
    return load(path)


if __name__ == "__main__":
    for men_entry in downlaod_men(MENType.NATURAL):
        print(men_entry)
