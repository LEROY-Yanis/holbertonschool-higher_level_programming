#!/usr/bin/python3
"""
Module that provides a function to return the JSON representation
of an object (string).
"""


class Student:

    def __init__(self, first_name, last_name, age):
        """
        Initializes a Student instance with first name,
        last name, and age.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Returns a dictionary representation of the Student instance.
        If attrs is a list of strings, only attributes 
        named in this list are returned.
        Otherwise, returns all attributes.
        """
        return self.__dict__

