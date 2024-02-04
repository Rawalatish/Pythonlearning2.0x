# Assignment Operators
name = "Pramod"

# it will store the value of variable literal to the identifier

# Unary Operator

age = +95
print(age)  # Op=> 95

temp_of_cold = -13
print(temp_of_cold)  # Op=> -13

# Not operator - Unary  | Applicable only for boolean

is_married = True
print(not is_married)  # Op=> False  | opposite value will give in return

# is operator   - Identifier operator

a = 5
b = 5
e = 6
print(a is b)  # Op=> True   | because same values are saved in same area of memory

print(a is c)  # Op => False

c = 5
d = 'box'

print(c is d)  # Op=> False

my_list = [1,2,3,4,]
my_list2 = [1,2,3,4,]

print(my_list is my_list2)   # Op => False     | because its a list and in list even same value the are save in different area of memory
