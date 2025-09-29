#!/usr/bin/python3
"""
Module that provides a function to return the JSON representation
of an object (string).
"""
import json


def from_json_string(my_str):
    """
    Returns the Python object represented by a JSON string.
    Uses the json module and json.loads().
    """
    return json.loads(my_str)
