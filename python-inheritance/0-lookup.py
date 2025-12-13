#!/usr/bin/python3
"""
This module contains a function that returns the list of
available attributes and methods of an object.
"""


def lookup(obj):
    """
    Returns a list of available attributes and methods of an object.

    Args:
        obj: The object to inspect.

    Returns:
        A list object containing the names of the object's attributes.
    """
    return dir(obj)
