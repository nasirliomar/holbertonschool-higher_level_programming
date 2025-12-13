#!/usr/bin/python3
"""Module: class_to_json"""


def class_to_json(obj):
    """
    Returns the dictionary description of an object
    for JSON serialization.
    """
    return obj.__dict__
