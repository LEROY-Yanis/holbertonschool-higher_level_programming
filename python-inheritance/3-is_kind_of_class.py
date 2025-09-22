#!/usr/bin/python3
"""
This module contains a function that checks if an object is an instance
of, or if the object is an instance of a class that inherited from,
the specified class.
"""


def is_kind_of_class(obj, a_class):
    """
    Checks if an object is an instance of a specified class or a subclass.

    Args:
        obj (any): The object to check.
        a_class (type): The class to compare against.

    Returns:
        bool: True if obj is an instance of a_class or a subclass,
              otherwise False.
    """
    return isinstance(obj, a_class)
