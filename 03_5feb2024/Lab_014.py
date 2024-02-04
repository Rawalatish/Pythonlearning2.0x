# String data type - its bunch of character and defined by "" or ''

name = "Pramod"
name2 = 'Pramod'

print(name)
print(name2)

print(type(
    name2))  # <class 'str'> | in interview they ask what is the tpye of this o/p then tell "str", not an string ,we know that str is shortform of string but still telll "str"

# Directory name e.g

dir = "C://abc.txt"  # Double quote
print(dir)  # o/p - C://abc.txt

dir2 = 'C://abc.txt'  # Single quote
print(dir2)  # o/p - C://abc.txt

# Now we see difference between single and double quote

dir3 = "C:\abc\efg.txt"   # used backward slash o/p - C:bc\efg.txt  | a is missing in o/p
print(dir3)    # o/p - C:bc\efg.txt

# in above e.g after \ 'a' define in different colour its special character here , after \ is there any charactor or word and its first letter is special char then it highlighted in differengt colour

dir4 = r"C:\abc\effffg.txt"
print(dir4)          # o/p -  C:\abc\effffg.txt | in that a is not missing because of we user 'r' at initial r for "raw string" and this keep the thing as it is
# this raw string 'r' is used in directory path and in dir path in API automation

#      Formate string f

s = 'Amit'
print(f"your name is {s}")   #your name is Amit | cury bracces replace with the value passed in it

first_name = "Ms"
last_name = 'Dhoni Thala'
age =37
isMarried = True

print(f"your name is {first_name} {last_name}")  # o/p - your name is Ms Dhoni Thala

print(f"your name is {first_name} {last_name}, your age is {age}, and you are married = {isMarried}")

print(f'your name is {first_name} {last_name}, your age is {age}, and you are married {isMarried}')  # with single quote | o/p - your name is Ms Dhoni Thala, your age is 37, and you are married True




