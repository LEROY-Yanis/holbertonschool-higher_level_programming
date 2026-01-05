#!/usr/bin/python3
"""
This module provides a function that prints a square with #.
It validates the size parameter before printing.
"""


def print_square(size):
    """Prints a square with the character #.
    size is the size length of the square.
    """
    if isinstance(size, float) and size < 0:
        raise TypeError("size must be an integer")
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for i in range(size):
        print("#" * size)
