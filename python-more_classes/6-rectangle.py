#!/usr/bin/python3
"""
This module defines a Rectangle class that tracks the number of instances.
"""


class Rectangle:
    """
    A class that defines a rectangle and keeps track of the number of instances.

    Attributes:
        number_of_instances (int): The number of active Rectangle instances.
    """

    number_of_instances = 0

    def __init__(self, width=0, height=0):
        """
        Initializes a new Rectangle instance, and increments the instance count.

        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

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
        Returns a string representation of the rectangle with '#' characters.
        """
        if self.width == 0 or self.height == 0:
            return ""

        rect_str = []
        for _ in range(self.height):
            rect_str.append("#" * self.width)
        return "\n".join(rect_str)

    def __repr__(self):
        """
        Returns a string representation to recreate a new instance.
        """
        return f"Rectangle({self.width}, {self.height})"

    def __del__(self):
        """
        Prints a message and decrements the instance count when a
        Rectangle is deleted.
        """
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1
