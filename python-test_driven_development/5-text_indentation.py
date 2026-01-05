#!/usr/bin/python3
"""
This module provides a function that prints text with indentation.
It adds 2 new lines after each '.', '?' and ':' characters.
"""


def text_indentation(text):
    """Prints text with 2 new lines after '.', '?' and ':'.
    Each printed line has no leading or trailing spaces.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    i = 0
    while i < len(text):
        print(text[i], end="")
        if text[i] in ".?:":
            print("\n")
            i += 1
            while i < len(text) and text[i] == " ":
                i += 1
            continue
        i += 1
