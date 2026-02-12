#!/usr/bin/python3
"""Module that defines a function for converting a class to JSON."""


def class_to_json(obj):
    """Return the dictionary description with simple data structure
    for JSON serialization of an object.

    Args:
        obj: An instance of a Class with serializable attributes
             (list, dictionary, string, integer and boolean).

    Returns:
        A dictionary representation of the object's attributes.
    """
    return obj.__dict__
