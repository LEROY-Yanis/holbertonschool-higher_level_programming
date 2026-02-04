#!/usr/bin/python3
"""Module that defines is_kind_of_class function."""


def is_kind_of_class(obj, a_class):
    """Check if an object is an instance of, or inherited from, a class.

    Args:
        obj: The object to check.
        a_class: The class to compare with.

    Returns:
        True if obj is an instance of a_class or inherited from it.
    """
    return isinstance(obj, a_class)
