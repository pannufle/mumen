"""A class to model a single entry (line) in the MEN dataset.

An entry contains a pair of words and a similarity score.
"""


class Pair:
    """A class to model a word pair."""

    def __init__(self, first, last):
        """Initialize with two words."""
        self._first = first
        self._last = last

    @property
    def first(self):
        """Getter for the first word in the Pair."""
        return self._first

    @property
    def last(self):
        """Getter for the last word in the Pair."""
        return self._last


class MENtry:
    """A class to process a line in the MEN dataset.

    Converts a MEN entry to an object containing a word pair and a similarity
    score.
    """

    def __init__(self, first, last, score=None):
        """Initialize MEN entry with Pair of words and sim score if given."""
        self._pair = Pair(first, last)
        if score:
            self._score = score

    @property
    def pair(self):
        """Getter for the Pair of words."""
        return self._pair

    @property
    def score(self):
        """Getter for the similarity score."""
        return self._score
