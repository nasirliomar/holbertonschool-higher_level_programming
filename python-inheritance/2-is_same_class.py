class Animal:
    pass

class Dog(Animal):  # Dog is a subclass of Animal
    pass

my_dog = Dog()

# Using isinstance() - includes subclasses
print(isinstance(my_dog, Dog))      # Output: True
print(isinstance(my_dog, Animal))   # Output: True (This is what we want to avoid)

# Using our is_same_class() function
print(is_same_class(my_dog, Dog))     # Output: True (Correct)
print(is_same_class(my_dog, Animal))  # Output: False (Correct)```
