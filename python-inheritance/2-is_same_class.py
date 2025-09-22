#!/usr/bin/python3
"""
This module contains a function to check if an object is exactly
an instance of a class.
"""


def is_same_class(obj, a_class):
    """
    Checks if an object is exactly an instance of the specified class.

    Args:
        obj (any): The object to check.
        a_class (type): The class to compare the object against.

    Returns:
        bool: True if the object is an exact instance of the class,
              otherwise False.
    """
    return type(obj) is a_class
