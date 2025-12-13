#!/usr/bin/python3
"""
This module contains a function that checks if an object is an instance of,
or an instance of a class that inherited from, a specified class.
"""


def is_kind_of_class(obj, a_class):
    """
    Returns True if the object is an instance of, or if the object is an
    instance of a class that inherited from, the specified class;
    otherwise False.

    Args:
        obj: The object to inspect.
        a_class: The class to check against.

    Returns:
        True if the object is a kind of the class, otherwise False.
    """
    return isinstance(obj, a_class)
