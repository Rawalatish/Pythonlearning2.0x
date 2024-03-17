class Person:          # First letter of class name should be in capital

                        # Class Varaibles/ Instance Var

    name = "Amit"                                # Empty variable is not allowed    | Hardcord value
    age = None

    def walk(self):
        a = 10  # Local variable
        print("Hi your name is ", self.name)
        print("Hi your age is ", self.age)
        print(a)


asmita = Person()                                     # It is Object
asmita.walk()

print("********")

pramod = Person()                                    # It is Object
pramod.walk()

# Here the value of both the object is same because of hardcored value.
#  So avoid this we use constructor