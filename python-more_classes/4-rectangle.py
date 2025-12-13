#!/usr/bin/python3
"""
This module defines a Rectangle class with official string representation.
"""


class Rectangle:
    """
    A class that defines a rectangle.
    """

    def __init__(self, width=0, height=0):
        """
        Initializes a new Rectangle instance.

        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """Gets the width of the rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        """Sets the width of the rectangle."""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Gets the height of the rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        """Sets the height of the rectangle."""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Returns the area of the rectangle."""
        return self.width * self.height

    def perimeter(self):
        """Returns the perimeter of the rectangle."""
        if self.width == 0 or self.height == 0:
            return 0
        return 2 * (self.width + self.height)

    def __str__(self):
        """
        Returns a user-friendly string representation of the rectangle
        with '#' characters. This is used by print() and str().
        """
        if self.width == 0 or self.height == 0:
            return ""

        rect_str = []
        for _ in range(self.height):
            rect_str.append("#" * self.width)
        return "\n".join(rect_str)

    def __repr__(self):
        """
        Returns an official string representation of the rectangle
        that can be used to recreate the object. This is used by repr().
        """
        return f"Rectangle({self.width}, {self.height})"
