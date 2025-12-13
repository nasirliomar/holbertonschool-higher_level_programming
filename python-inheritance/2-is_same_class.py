#!/usr/bin/python3
"""
This module contains a function that checks if an object is exactly
an instance of a specified class.
"""


def is_same_class(obj, a_class):
    """
    Returns True if the object is exactly an instance of the specified class;
    otherwise False.

    Args:
        obj: The object to inspect.
        a_class: The class to match the object's type against.

    Returns:
        True if obj is exactly an instance of a_class, otherwise False.
    """
    return type(obj) is a_class
