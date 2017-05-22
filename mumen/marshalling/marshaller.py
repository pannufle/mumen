"""Unmarshalling dictionaries .xml files."""

import logging
from mumen.marshalling.models import jmdict

__all__ = ['unmarshall']

logger = logging.getLogger(__name__)


def unmarshall(input_file):
    with open(input_file, 'r', encoding='utf-8') as input_stream:
        return jmdict.CreateFromDocument(input_stream.read())
