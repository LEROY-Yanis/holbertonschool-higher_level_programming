#!/usr/bin/env python3
"""Module that demonstrates mixin classes with a Dragon."""


class SwimMixin:
    """Mixin class that provides swimming ability."""

    def swim(self):
        """Print that the creature swims."""
        print("The creature swims!")


class FlyMixin:
    """Mixin class that provides flying ability."""

    def fly(self):
        """Print that the creature flies."""
        print("The creature flies!")


class Dragon(SwimMixin, FlyMixin):
    """A class representing a dragon with swim and fly abilities."""

    def roar(self):
        """Print that the dragon roars."""
        print("The dragon roars!")
