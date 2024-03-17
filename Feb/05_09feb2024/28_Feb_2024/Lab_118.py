                                 # Multiple Inheritance

# F,M -> S

class Father:
    def father_money(self):
        return "5"

    def home(self):
        print("this is from father")

class Mother:
    def mother_money(self):
        return "2"

    def home(self):
        print("This is from mother")


class Son(Father, Mother):
     pass


son = Son()
print(son.father_money())
print(son.mother_money())
print(son.home())                 # Op= None           # Diamond problem | which home method will get called? father, mother or son its confusion hence its called diamond problem

print("******************************")
# MRO - Method Resolution Order

                                     # How to resolve this


class Father1:
     def father_money1(self):
         return "5"

     def home1(self):
         return "This is from the Father"


class Mother1:
     def mother_money1(self):
         return "2"

     def home1(self):
         return "This is from the Mother"

class Son1(Mother1, Father1):
    pass
     # def home1(self):
     #     return "This is from the Son"


son1 = Son1()
# print(Son1.mro())
# print(son1.father_money1())
# print(son1.mother_money1())
print(son1.home1())                                               # Something is wrong in this program
