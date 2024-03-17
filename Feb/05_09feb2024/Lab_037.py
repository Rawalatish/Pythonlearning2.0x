# problem statement - Find the max between 3 numbers

num1 = int(input("Enter num1"))
num2 = int(input("Enter num2"))
num3 = int(input("Enter num3"))

# By using max function
# max_mum = max(num1, num2, num3)
#
# print("it is the maximum number", max_mum)

# By using if condition

if num1 > num2 and num1 > num3:
    print("Max is", num1)
elif num2 > num1 and num2 > num3:
    print("Max is ", num2)
else:  # When there is no condition left then use else not a elif
    print("Max is ", num3)
