#!/usr/bin/python3
"""Module that defines a Square class."""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """A class representing a square, inherits from Rectangle."""

    def __init__(self, size):
        """Initialize a Square with size.

        Args:
            size: The size of the square.
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
