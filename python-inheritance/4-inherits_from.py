#!/usr/bin/python3
"""
This module defines a function that checks if an object is an instance of
a class that inherited (directly or indirectly) from a specified class.
"""


def inherits_from(obj, a_class):
    """
    Returns True if the object's class is a subclass of the specified class.

    This function returns False if the object is an instance of the exact
    class specified.

    Args:
        obj: The object to inspect.
        a_class: The potential parent class.

    Returns:
        True if the object is an instance of a subclass of a_class,
        otherwise False.
    """
    # The object must be an instance of the class or its subclass
    # AND its type cannot be the exact class.
    return isinstance(obj, a_class) and type(obj) is not a_class
