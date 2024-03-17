# *args and **kargs

# def f1(a, b, c):
#     return a + b + c
#
#
# f1(1)     # here i have only pass 1 value i.e. goes into "a" agrument and run | O/p => error saying TypeError: f1() missing 2 required positional arguments: 'b' and 'c'

#  we we want to handle it then provide the value in the define function so it will be default value and will replace when we pass the value in calling area other wise it will take default value
# and error will not come


def f1(a=1, b=1, c=1):
    return a + b + c


x = f1()
print(x)
f1(2)
f1(1, 2)
f1(1, 2, 3)
f1(a=10, b=20, c=30)


# r = f1(c=1, a=2, b=90)  we can change the position but this will create huge confusion | not re-commanded
# print(r)
#############################################

# *args =>

# def sum(a, b, c, d, e):
#     return a + b + c + d + e
#
#
# r = sum(1, 2, 3)
# r = sum(1, 2, 3, 4, 5)
# print(r)

def print_argument(*args):
    for i in args:
        print(i,)


print_argument(1)
print_argument(1, 2)
print_argument(1, 2, 3)
print_argument(1, 2, 3, 4)
print_argument(1,2,3,4,8,9,88)

print(1,2,3,4,8,9,88)
