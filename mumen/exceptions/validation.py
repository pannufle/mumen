#! /usr/bin/python3
"""Simple exception for validation process.

author: Martino Ferrari
author_email: martino.ferrari@etu.unige.ch
"""


class ValidationException(Exception):
    """Simple Exception for Mumen Config validation.

    It will be used to raise exception for wrong or incomplete config.
    """

    def __init__(self, msg):
        """Inizialize validation error.

        Args:
            msg: error message as string.

        """
        Exception.__init__(self, msg)
