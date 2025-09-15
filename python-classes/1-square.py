#!/usr/bin/python3
"""
Define a class called Square
"""


class Square:
    """
    Constructor method to initialize the square
    """
    def __init__(self, size):
        """
        Private attribute to store the size of the square
        (Note: here it's hardcoded to 3, ignoring the 'size' parameter)
        """
        self.__size = size
