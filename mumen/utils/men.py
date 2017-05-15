"""MEN Utilities.

This module contains many utilities to load, create and store MEN Files:
https://staff.fnwi.uva.nl/e.bruni/MEN.
"""


def decode(row):
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
    return (men_row[0], men_row[1], float(men_row[2]))


def encode(entry):
    """Encode an MEN entry to .

    Args:
        entry: MEN entry in form of dictionary
    Returns:
        MEN entry string

    """
    return '{} {} {}'.format(entry[0],
                             entry[1],
                             entry[2])
