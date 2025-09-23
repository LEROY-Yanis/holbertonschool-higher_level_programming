#!/usr/bin/python3
"""
Module 1-my_list
Defines a class MyList that inherits from list
"""

def inherits_from(obj, a_class):
	"""
	Returns True if obj is an instance of a class that inherited from a_class
	(directly or indirectly), but not if obj is an instance of a_class itself.
	"""
	return isinstance(obj, a_class) and type(obj) is not a_class
