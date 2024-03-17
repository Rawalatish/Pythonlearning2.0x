# Factorial
# n = 5
# 5*4*3*2*1 = 120

number = int(input("Enter the factorial number\n"))
if number < 0:
    print("Factorial")
else:
    fact = 1
    for i in range(1,number + 1):
        fact = fact * i

print("factorial is =", fact)
