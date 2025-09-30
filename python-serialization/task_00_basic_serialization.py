#!/usr/bin/python3
"""
Basic serialization module for saving/loading Python dictionaries to/from JSON files.
"""

import json

def serialize_and_save_to_file(data, filename):
    """
    Serializes a Python dictionary and saves it to a JSON file.
    If the file exists, it will be replaced.
    """
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(data, f)

def load_and_deserialize(filename):
    """
    Loads and deserializes a JSON file to recreate the Python dictionary.
    Returns the dictionary.
    """
    with open(filename, 'r', encoding='utf-8') as f:
        return json.load(f)
