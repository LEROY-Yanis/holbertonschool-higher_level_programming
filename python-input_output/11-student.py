#!/usr/bin/python3
"""
Defines a Student class with JSON serialization and deserialization.
"""


class Student:
    """Represent a student."""

    def __init__(self, first_name, last_name, age):
        """Initialize a new Student instance."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Retrieve a dictionary representation of the Student instance.

        If attrs is a list of strings, only those attributes are included.
        """
        if isinstance(attrs, list) and all(isinstance(s, str) for s in attrs):
            return {k: getattr(self, k) for k in attrs if hasattr(self, k)}
        return self.__dict__

    def reload_from_json(self, json):
        """Replace all attributes of the Student instance using a dictionary."""
        for key, value in json.items():
            setattr(self, key, value)
