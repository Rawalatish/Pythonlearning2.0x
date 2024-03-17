#                                           Method Overriding


# child always override the parent functions
# super means call my parent function


class Animal:

    def __init__(self):
        pass

    def sound(self):
        print("Animal Sound")


class Dog(Animal):

    def __init__(self):
        pass

    def sound(self):
        # super().sound()                            # Super Keyword   | by using this we can call funtions of whos is super
        print("Dog Sound")


# animal = Animal()
# animal.sound()                                  # Op = Animal Sound  | from parent

dog = Dog()
dog.sound()                                       # op= Dog Sound