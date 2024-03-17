# Car -    we are taking Car as class
# Objects - Tesla, Lambo


class Car:
    name = None
    color = None
    model = None
    speed = None
    engine = None                           # ^ All of these attributes

    # self is a special variable that is used within the context of object-oriented programming (OOP).
    # 'self' is a reference to the instance of a class
    # By using 'self' we can access the attributes( variables) in the class
    # access and manipulate the attributes and methods of that instance / Object
    # we can have different methods

    def start_engine(self):
        print("Starting engine")

    def drive(self):
        print("Drive")

    def car_break(self):
        print("Break")

    def who_is_driving(self):
        print("I am driving -> " + self.name)


#Objects

tesla_obj_ref = Car()                           # here object reference is tesla_obj_ref and Object is Car()
lambo_obj_ref = Car()

tesla_obj_ref.name = "Tesla"
lambo_obj_ref.name = "Lambo"

tesla_obj_ref.who_is_driving()
lambo_obj_ref.who_is_driving()
tesla_obj_ref.start_engine()