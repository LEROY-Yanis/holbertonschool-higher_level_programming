#!/usr/bin/python3
"""Module that defines inherits_from function."""


def inherits_from(obj, a_class):
    """Check if object is an instance of a class that inherited from a_class

    Args:
        obj: The object to check.
        a_class: The class to compare with.

    Returns:
        True if obj inherited from a_class (not direct instance).
    """
    return isinstance(obj, a_class) and type(obj) is not a_class
