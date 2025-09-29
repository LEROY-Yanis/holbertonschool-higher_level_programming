#!/usr/bin/python3
"""
Module that provides a function to return the JSON representation
of an object (string).
"""
import json


def to_json_string(my_obj):
    """
    Returns the JSON representation of an object (string).
    Uses the json module and json.dumps().
    """
    return json.dumps(my_obj)
