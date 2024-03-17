# Global variable in python

# Fibonacci series = > 0, 1, 1, 2, 3, 5, 8, 13, 21 .....

# a = 10
# b = 12
# a, b = a, a+b
# print(a, b)

a, b = 0, 1
while a < 10:
    print(a, end= " ")       # we use here 'end=' | because o/p will come into one line
    a, b = b, a+b



