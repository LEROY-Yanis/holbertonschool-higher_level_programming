#!/usr/bin/env python3
"""Custom object serialization using pickle module."""

import pickle


class CustomObject:
    """A custom class with serialization capabilities."""

    def __init__(self, name, age, is_student):
        """Initialize the CustomObject.

        Args:
            name: A string representing the name
            age: An integer representing the age
            is_student: A boolean indicating student status
        """
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        """Display the object's attributes."""
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Is Student: {self.is_student}")

    def serialize(self, filename):
        """Serialize the current instance to a file.

        Args:
            filename: The filename to save the serialized object
        """
        try:
            with open(filename, 'wb') as f:
                pickle.dump(self, f)
        except Exception:
            return None

    @classmethod
    def deserialize(cls, filename):
        """Deserialize an instance from a file.

        Args:
            filename: The filename to load the serialized object from

        Returns:
            An instance of CustomObject or None if an error occurs
        """
        try:
            with open(filename, 'rb') as f:
                return pickle.load(f)
        except Exception:
            return None
