#  WAP for find square root and cube root
import math

number = float(input("enter the  number"))

square = number ** 2
print(square)

square_root = math.sqrt(number)
print(square_root)

cube = number ** 3
print(cube)

# or
cube2 = math.pow(number, 3)
print(cube2)
