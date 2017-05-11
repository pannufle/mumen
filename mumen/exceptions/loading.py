#! /usr/bin/python3
"""Simple exception for loading process."""


class ConfigException(Exception):
    """Simple Exception for Mumen translation process."""

    def __init__(self, msg):
        """
        Inizialize validation error.

        Args:
            msg: error message as string.

        """
        Exception.__init__(self, msg)
