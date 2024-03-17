
                                   # Encapsulation

# - bind the data v and methods(hide the important variables)
# Data members / Class variable -
# Functions - they are closed within a single blueprint
# Wrapping or binding the data variables with the methods

class Car:
    name = None                        # Data variables

    # password = "123"
    # 3 different types of Data Members / class variables

    def __init__(self):
        self.public_var = "public"                  # Public Variable - Anyone can access it
        self._protected_var = "protected123"        # protected variable - here we use single underscore'_' at start
        self.__private_var = "pass@123"             # Private variable - here we use double underscore'__' at start
        self.__password ="pas@123"
     #   self.band ="bandbaja"

    def _protected_method(self):
        print("Protected!")

    def __private_method(self):
        print("Protected!")
        print()

    def printName(self):
        print("I am allowed to use the private variable becz I am in class " + self.__password)      # encapsulation


xuv = Car()
xuv.printName()                                  # in that method we use private variable and accessed to call outside
                                                 # this is the encapsulation
xuv._protected_method()
# xuv.__private_method()                      #  private method is not allowed to call | this should not be allowed


# lambo= Car("Lambo")
# lambo.printName()

print(xuv.public_var)
print(xuv._protected_var)
# print(xuv.__password)                        # private variable is not allowed to call
# print(xuv.printName())