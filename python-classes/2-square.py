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
