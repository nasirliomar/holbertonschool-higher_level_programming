#!/usr/bin/python3
"""Module: Student"""


class Student:
    """Student class"""

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Returns the dictionary representation of a Student.
        If attrs is a list of strings, only those attributes are returned.
        """
        if isinstance(attrs, list):
            return {
                key: value
                for key, value in self.__dict__.items()
                if key in attrs
            }
        return self.__dict__
