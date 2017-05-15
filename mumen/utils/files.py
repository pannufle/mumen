"""Files utilities for MuMEN.

This module provides basic utilities for handling files and directories
"""

import os


__all__ = ['get_filename']


def get_filename(input_file):
    """Get the basename of a filefiles without the extension."""
    return os.path.splitext(os.path.basename(input_file))[0]
