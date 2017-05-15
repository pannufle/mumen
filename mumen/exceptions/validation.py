"""Simple exception for the validation process.

Details
"""

__all__ = ['ValidationError']


class ValidationError(Exception):
    """A specific exception for validation."""

    def __init__(self, message):  # pylint:disable=W0235
        """Init function."""
        super().__init__(message)
