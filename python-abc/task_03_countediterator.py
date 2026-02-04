#!/usr/bin/env python3
"""Module that defines a CountedIterator class."""


class CountedIterator:
    """An iterator that counts the number of items iterated."""

    def __init__(self, iterable):
        """Initialize the CountedIterator with an iterable."""
        self.iterator = iter(iterable)
        self.count = 0

    def get_count(self):
        """Return the number of items that have been iterated."""
        return self.count

    def __iter__(self):
        """Return the iterator object."""
        return self

    def __next__(self):
        """Return the next item and increment the counter."""
        item = next(self.iterator)
        self.count += 1
        return item
