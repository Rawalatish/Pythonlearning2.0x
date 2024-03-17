# Take the 2 number from the user and we want to add them
# Step1 =Take input
# step2 = Sum

num1 = input("Enter the first number")
num2 = input("Enter the second number")
print(num1)
print(num2)

print(type(num1))   # o/p = <class 'str'> // its not coming into integer value

num3 = num1 + num2
print(num3)  # o/p 4585 // its going into string hence its not adding instead of giving string in concat

# hence we need to conver this num123 into integer

num3 = int(num1) + int(num2)  # for this we used "int" function i.e integer method

print(type(num3), "num3 =", num3) # if two values type is integer then addition of this also integer

# there many way conver string into integer ( one thing can be done in 2-3 different way)

num4 = int(input(" enter again first number"))
num5 = int(input(" enter again second number"))

print(type(num4))  # o/p <class 'int'>

