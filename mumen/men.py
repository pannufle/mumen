#! /usr/bin/python3
"""MEN Utilities
This module contains many utilities to load, creante and store MEN Files:
https://staff.fnwi.uva.nl/e.bruni/MEN.
"""
import requests
import zipfile
import os


def downlaod_men():
    """Download the last version of the MEN data-set from:
    https://staff.fnwi.uva.nl/e.bruni/resources

    Returns:
        The MEN structure
    """
    reponse = requests.get(
                "https://staff.fnwi.uva.nl/e.bruni/resources/MEN.zip",
                stream=True)
    if reponse.status_code == 200:
        if not os.path.isdir(".tmp/"):
            os.mkdir(".tmp")
        with open(".tmp/MEN.zip", 'wb') as f:
            for chunk in reponse:
                f.write(chunk)
        with zipfile.ZipFile(".tmp/MEN.zip", "r") as zip_ref:
            zip_ref.extractall(".tmp/")
        men = []
        with open(".tmp/MEN/MEN_dataset_natural_form_full", "r") as f:
            for men_row in f:
                men_row = men_row.strip().split()
                men_entry = {
                    "word_L": men_row[0],
                    "word_R": men_row[1],
                    "similarity": float(men_row[2])
                }
                men.append(men_entry)
        return men
    else:
        raise Exception("Download failed ({}) : {}".format(reponse.status_code,
                                                           reponse.text))


def load(path: str) -> list:
    """Function to load a MEN FILE

    Args:
        path: path to the MEN file to load.

    Returns:
        the MEN Structure.
    """
    men = []
    with open(path, "r") as f:
        for men_row in f:
            men_row = men_row.strip().split()
            men_entry = {
                "word_L": men_row[0],
                "word_R": men_row[1],
                "similarity": float(men_row[2])
            }
            men.append(men_entry)
    return men


def store(men: list, path: str):
    """Function to sture a MEN list to file.

    Args:
        param men: men list structure to save.
        param path: path to the file where to store the MEN.
    """
    with open(path, "w") as f:
        for entry in men:
            f.write(
                f'{entry["word_L"]} {entry["word_R"]} {entry["similarity"]}\n'
                )


if __name__ == "__main__":
    print(downlaod_men())
