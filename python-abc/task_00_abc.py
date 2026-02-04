#!/usr/bin/env python3
"""Module that defines an abstract Animal class and its subclasses."""
from abc import ABC, abstractmethod


class Animal(ABC):
    """Abstract class representing an animal."""

    @abstractmethod
    def sound(self):
        """Abstract method that should return the sound of the animal."""
        pass


class Dog(Animal):
    """A class representing a dog."""

    def sound(self):
        """Return the sound a dog makes."""
        return "Bark"


class Cat(Animal):
    """A class representing a cat."""

    def sound(self):
        """Return the sound a cat makes."""
        return "Meow"
