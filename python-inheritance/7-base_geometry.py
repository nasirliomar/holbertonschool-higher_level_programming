#!/usr/bin/python3
"""Module: BaseGeometry"""


class BaseGeometry:
    """BaseGeometry class"""

    def area(self):
        """Raises an Exception because area is not implemented."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validates that value is an integer > 0.

        Args:
            name (str): name of the value (used in error messages)
            value: value to validate

        Raises:
            TypeError: if value is not an integer
            ValueError: if value <= 0
        """
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
