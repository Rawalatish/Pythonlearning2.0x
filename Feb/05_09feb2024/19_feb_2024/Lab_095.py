# Class & Objects in Python
# Class -  contains Attributes and Behaviour

# Person(class) -> Object =  Ram, Pramod, Shreeram      |here we are defined class as person

class Person:
    # Attributes  -> also called as Data members     | These are the person's attributes
    name = None
    age = None
    id = None
    phone_no = None


    # Behaviour -> also called as Methods (Method is not the functions)  |  Functions are not used in the class or classes

    # Whenever function is used in the class, it is called as Method  | IMP
    def talk(self):
        print("I cam talk")

    def another(self):
        print("I am a Method")


    def sleep(self, name):
        print("I am a Method!!")
        print("Sleep", name)

    def walk(self):
        return "I am walking"


def anotherf():
    print("I am another f(n)")


#                                          Object creation
# Objects - ClassName()

shreeram = Person()
shreeram.name = "Sheeram"
print(shreeram.name)
shreeram.talk()  # This belong Shreeram

pramod = Person()

amit = Person()

# Nothing is THERE, SO CLEAN THE memory    | After the line no 46
# exit the program