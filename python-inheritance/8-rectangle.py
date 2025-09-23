#!/usr/bin/python3
"""BaseGeometry class with area and integer_validator methods"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry

class Rectangle(BaseGeometry):
	"""Rectangle that inherits from BaseGeometry"""

	def __init__(self, width, height):
		super().__init__()
		self.integer_validator("width", width)
		self.integer_validator("height", height)
		self.__width = width
		self.__height = height
