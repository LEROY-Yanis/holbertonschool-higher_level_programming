#!/usr/bin/python3
"""
Module that provides a function to return the JSON representation
of an object (string).
"""


def class_to_json(obj):
    """
    Returns the dictionary description of a simple data structure for JSON serialization.
    """
    return obj.__dict__
