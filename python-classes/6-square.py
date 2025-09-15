#!/usr/bin/python3
"""
This module defines the Square class.
"""


class Square:
    """
    Represents a square with size and position attributes.
    """

    def __init__(self, size=0, position=(0, 0)):
        """
        Initialize a new Square instance.

        Args:
            size (int, optional): Size of the square (default is 0).
            position (tuple, optional): A tuple of two positive integers
            representing the horizontal and vertical offsets(default is (0, 0))

        Raises:
            TypeError: If size is not an integer, or if position is not a tuple
                of 2 positive integers.
            ValueError: If size is less than 0.
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """
        Get the size of the square.

        Returns:
            int: The size of the square.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Set the size of the square with validation.

        Args:
            value (int): The new size.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """
        Get the position of the square.

        Returns:
            tuple: A tuple of two positive integers.
        """
        return self.__position

    @position.setter
    def position(self, value):
        """
        Set the position of the square with validation.

        Args:
            value (tuple): A tuple of two positive integers.

        Raises:
            TypeError: If value is not a tuple of 2 positive integers.
        """
        if (
            not isinstance(value, tuple) or
            len(value) != 2 or
            not all(isinstance(num, int) for num in value) or
            not all(num >= 0 for num in value)
        ):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """
        Compute the area of the square.

        Returns:
            int: The area of the square.
        """
        return self.__size * self.__size

    def my_print(self):
        """
        Print the square with the character '#',
        applying the position offsets.

        If size is 0, prints an empty line.
        """
        if self.__size == 0:
            print()
            return

        # Vertical offset
        for _ in range(self.__position[1]):
            print()

        # Horizontal offset + square printing
        for _ in range(self.__size):
            print(" " * self.__position[0] + "#" * self.__size)
