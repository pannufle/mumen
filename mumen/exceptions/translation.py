#! /usr/bin/python3
"""Simple exception for translation process.

author: Martino Ferrari
author_email: martino.ferrari@etu.unige.ch
"""


class TException(Exception):
    """Simple Exception for Mumen translation process."""

    def __init__(self, msg):
        """Inizialize validation error.

        Args:
            msg: error message as string.

        """
        Exception.__init__(self, msg)
