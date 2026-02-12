#!/usr/bin/python3
"""Module that contains the write_file function."""


def write_file(filename="", text=""):
    """Writes a string to a text file and returns the number of characters."""
    with open(filename, mode="w", encoding="utf-8") as f:
        return f.write(text)
