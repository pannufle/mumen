"""Module to validate the Translation config section."""
import mumen.validation.validators.men_fileinout as meninout


def validate(module):
    """Validate the Translation section.

    Args:
        module: Translation config section
    """
    meninout.validate(module['source'])
    meninout.validate(module['target'])
    # __validate_translator__(module['translator'])
