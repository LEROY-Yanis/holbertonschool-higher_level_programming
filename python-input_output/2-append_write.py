#!/usr/bin/python3
"""Module that contains the append_write function."""


def append_write(filename="", text=""):
    """Appends a string at the end of a text file and returns chars added."""
    with open(filename, mode="a", encoding="utf-8") as f:
        return f.write(text)
