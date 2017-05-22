#! /usr/bin/python3
"""Mumen main script.

Mumen read and translate MEN files and then use it to generate YACAB surveys.
"""
import sys
import argparse
import logging
import yaml

import mumen.translation.translator as translator
import mumen.validation.validator as validator
import mumen.utils.files as futils
from mumen.exceptions.input import InvalidInputError
from mumen.exceptions.method import InvalidMethodError
from mumen.exceptions.parameter import InvalidParameterError
from mumen.exceptions.validation import ValidationError
from mumen.utils.immutables import ImmutableConfig


logging.basicConfig(format='%(levelname)s - %(message)s',
                    level=logging.DEBUG)
logger = logging.getLogger(__name__)


def main():
    """Launch the MuMen application with the provided config file."""
    parser = argparse.ArgumentParser(
        description='Translate MEN and generate YACAB questions.')
    parser.add_argument(
        'config', metavar='config', type=str,
        help='YML configuration to load.')
    logger.info('Welcome to MuMEN!')
    args = parser.parse_args()
    config_file = args.config
    logger.info('Launching Nima with config: {}'.format(config_file))

    try:
        lang_iso_code = futils.get_filename(config_file)
        validator.validate_iso639_1_code(lang_iso_code)

        with open(config_file, 'r') as config_stream:
            config = yaml.safe_load(config_stream)
            logger.debug(config)
            iconfig = ImmutableConfig(config)
            if iconfig['translate']:
                translator.translate_dataset(lang_iso_code,
                                             iconfig['translation'])
    except (ValidationError, InvalidParameterError, InvalidMethodError,
            InvalidInputError) as err:
        logger.error(err)
        logger.error('Exiting MuMen')
        sys.exit(1)  # exit with error code 1 when program errors


if __name__ == "__main__":
    main()
