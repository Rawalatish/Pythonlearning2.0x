#                Multiple parameter class

class Mul_para:
    name = None  # Class Variable

    def print_information(self, first_name, last_name, age):
        a = 10  # Local Variable  we can't access local variable outside the class
        print("Your name is ", first_name, last_name, age)
        print(self.name)


obj_ref = Mul_para()
obj_ref.print_information("Amit", "Sharma", 68)