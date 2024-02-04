# Condition

# age > 18 you are allow to vote
# age < 18 you are not allow to vote

# age22 = input("Enter your age")   # this will reture the String, so we have to conver it into integer so we use int function

age = int(input("Enter your age"))

# syntax for if condition  > if condition:    > its return True or False

if age > 18:  # no need to use bracket until there are multiple condition
    print(" your are allow to vote")
else:
    print("your are not allow to vote")

a = 8

# if a = 5:   This will not return the condition True or False

if a == 5:
    print("hi")
else:
    print("bye")

x = 20
y = 10

# in two variable we have 3 conditions   | in multiple contion we can use "elif"
# x > y
# y > x
# x ==y

if x > y:
    print("x is greater than y")

elif x < y:
    print(" x is less than y")

else:
    print(" x == y")
