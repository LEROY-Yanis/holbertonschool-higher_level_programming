#!/usr/bin/python3
"""
Module that provides a function to return the JSON representation
of an object (string).
"""
import json


def load_from_json_file(filename):
    """
    Read an object to a text file using a JSON representation.
    Uses the json module and json.load().
    """
    with open(filename, "r", encoding="utf-8") as f:
        return json.load(f)
