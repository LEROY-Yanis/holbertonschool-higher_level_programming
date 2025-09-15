#!/usr/bin/python3
"""
Define a class called Square
"""


class Square:

    """
    Constructor method with a default size of 0
    """
    def __init__(self, size=0):

        """
        Check if 'size' is an integer
        """

        if not isinstance(size, int):
            raise TypeError("size must be an integer")

        """
        Check if 'size' is non-negative
        """

        if size < 0:
            raise ValueError("size must be >= 0")

        """
        Store the validated size as a private attribute
        """

        self.__size = size

    @property
    def size(self):
        """
        Getter method for the size attribute.

        Returns:
            int: The current size of the square.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Setter method for the size attribute with validation.

        Args:
            value (int): The new size of the square.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is negative.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    """
    Method to calculate the area of the square
    """

    def area(self):

        """
        The area of a square is size squared
        """

        return self.__size * self.__size
