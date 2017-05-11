#! /usr/bin/python3
"""Base dictionary class."""
from abc import abstractmethod


class BaseDict:
    """Base dictionary class."""

    def __init__(self, source_lang, target_lang):
        """Initialize WordNet dictionary."""
        self.__source__ = source_lang.to_wnet_lang_id()
        self.__target__ = target_lang.to_wnet_lang_id()

    def source(self):
        """Get source language."""
        return self.__source__

    def target(self):
        """Get target language."""
        return self.__target__

    @abstractmethod
    def translate(self, word):
        """Translate word."""
