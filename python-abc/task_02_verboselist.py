#!/usr/bin/env python3
"""Module that defines a VerboseList class extending the built-in list."""


class VerboseList(list):
    """A list subclass that prints notifications on modifications."""

    def append(self, item):
        """Add an item to the list and print a notification."""
        super().append(item)
        print("Added [{}] to the list.".format(item))

    def extend(self, items):
        """Extend the list with items and print a notification."""
        items_list = list(items)
        super().extend(items_list)
        print("Extended the list with [{}] items.".format(len(items_list)))

    def remove(self, item):
        """Remove an item from the list and print a notification."""
        print("Removed [{}] from the list.".format(item))
        super().remove(item)

    def pop(self, index=-1):
        """Pop an item from the list and print a notification."""
        item = self[index]
        print("Popped [{}] from the list.".format(item))
        return super().pop(index)
