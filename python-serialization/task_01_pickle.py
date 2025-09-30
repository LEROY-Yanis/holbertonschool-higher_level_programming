#!/usr/bin/python3
"""
Module for serializing and deserializing CustomObject instances using pickle.
Provides methods to save an object to a file and load it back.
"""
import pickle


class CustomObject:
    def __init__(self, name, age, is_student):
        """
        Initialize the object with name, age, and student status
        """
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        """
        Print the object's attributes in a formatted way
        """
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Is Student: {self.is_student}")

    def serialize(self, filename):
        """
        Serialize the object and save it
        to a file using pickle
        """
        try:
            with open(filename, 'wb') as f:
                pickle.dump(self, f)
        except Exception:
            return None

    @classmethod
    
    def deserialize(cls, filename):
        """
        Deserialize an object from a file
        and return it (or None if error)
        """
        try:
            with open(filename, 'rb') as f:
                obj = pickle.load(f)
            if isinstance(obj, cls):
                return obj
            return None
        except Exception:
            return None
