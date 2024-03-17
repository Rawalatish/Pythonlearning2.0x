# Lambda Express  - it is basically create to help user
# it can be convert any function in one-liner

# we rarely use it | it is good to know so

def say_hello():
    print("hello")


say_hello()

# def double_my_salary(salary):        # in this we have multiple number of lines code from 11 to 16 | so we can do
#                                        this by using lambda function return salary * 2
#
#
# result = double_my_salary(15000)
# print(result)

result2 = lambda salary: salary * 2     # single line code | what we defined in define fun this is we defined
#                                       in one-lien by using lambda
print(result2(10))

# print("this is by using lambda", result2(10))

power_of = lambda num: num**2
print(power_of(5))

sum = lambda a, b, c: a + b -c               # lamda with multiple arguments
print(sum(4,8,3))

say_my_name = lambda name: print("Your name is ", name)
say_my_name("Pramod")
