#!/usr/bin/python3
"""
Core Function Definition for the Module
"""


def read_file(filename=""):
    """
    Reads a text file (UTF8) and prints its content to stdout.
    """
    with open(filename, encoding="utf-8") as f:
        read_data = f.read()
        print(read_data, end="")
