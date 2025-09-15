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

    @property
    def position(self):
        """
        Returns the position of the square.

        The position is expected to be a tuple of two non-negative integers
        representing horizontal and vertical offsets when printing the square.
        """

        return self.__position

    @position.setter
    def position(self, value):
        """
        Sets the position of the square.

        Args:
            value (tuple): A tuple of two non-negative integers (x, y).

        Raises:
            TypeError: If value is not a tuple of 2 non-negative integers.
        """
        if (not isinstance(value, tuple) or 
            len(value) != 2 or
            not all(isinstance(num, int) for num in value) or
            not all(num >= 0 for num in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    """
    Method to calculate the area of the square
    """

    def area(self):

        """
        The area of a square is size squared
        """

        return self.__size * self.__size

    """
    Method to print the square using the '#' character
    """
    def my_print(self):
        """
        If size is 0, just print a newline
        """

        if self.__size == 0:
            print()
            return

        """
        Vertical offset
        """

        for i in range(self.__position[1]):
            print()

        """
        Horizontal offset + square printing
        """

        for i in range(self.__size):
            print(' ' * self.__size[0] + "#" * self.__size)
