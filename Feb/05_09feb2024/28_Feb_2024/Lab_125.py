# Ecap
# Inheritance
# poly ( method overriding, method overloading)


#                                          Abstraction
#  It is a concept of OOPs
# Abstraction =  Hiding the details and showing what is required

# Do you know How engine is started?
# How gear box was managed?

# hide the implementation and show only the important details
# 1. Abstract Base Class
# 2. Abstract base Methods

from abc import ABC, abstractmethod                   # Abstract base class


class Animal(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod                                  # incomplete method
    def sound(self):
        pass


class Dog(Animal):
    def sound(self):
        return "Bow Bow"


class Cat(Animal):
    def sound(self):
        return "Meow "


dog = Dog("Rancho")
print(dog.sound())

cat = Cat("CAT")
print(cat.sound())
