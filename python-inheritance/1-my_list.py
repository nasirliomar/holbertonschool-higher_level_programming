#!/usr/bin/python3
"""
This module defines a class MyList that inherits from the built-in list class.
"""


class MyList(list):
    """
    A class that inherits from list and adds a method to print a sorted
    version of the list.
    """

    def print_sorted(self):
        """
        Prints the elements of the list in ascending sorted order.
        """
        print(sorted(self))
