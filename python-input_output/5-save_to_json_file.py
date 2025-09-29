#!/usr/bin/python3
"""
Module that provides a function to return the JSON representation
of an object (string).
"""
import json


def save_to_json_file(my_obj, filename):
    """
    Writes an object to a text file using a JSON representation.
    Uses the json module and json.dump().
    """
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(my_obj, f)