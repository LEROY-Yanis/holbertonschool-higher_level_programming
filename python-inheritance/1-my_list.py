#!/usr/bin/python3
"""
Module 1-my_list
Defines a class MyList that inherits from list
"""


class MyList(list):
    """Custom list class with extra method to print sorted list"""

    def print_sorted(self):
        """
        Prints the list, but sorted in ascending order.
        Does not modify the original list.
        """
        print(sorted(self))
