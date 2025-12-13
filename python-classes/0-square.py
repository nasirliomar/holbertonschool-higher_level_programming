#!/usr/bin/env python3

class Square:
    def __init__(self, size):
        self.__size = size

if __name__ == "__main__":
    my_square = Square(5)
    print("A Square object was created.")
    print("Internal dictionary of the object:", my_square.__dict__)
