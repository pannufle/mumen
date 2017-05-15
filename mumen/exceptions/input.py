"""Docstring.

Details
"""

__all__ = ['InvalidInputError']


class InvalidInputError(Exception):
    """A specific exception for invalid input."""

    def __init__(self, message):  # pylint:disable=W0235
        """Init function."""
        super().__init__(message)
