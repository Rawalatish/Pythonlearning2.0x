# String Concat

str1 = 'hello'
str2 = 'word'
str3 = str1 + str2     # Op => helloword

print(str3)

name = 'pramod'
age = 65

#r = name + age

#print(r)     # Op=>   # Op=> TypeError: can only concatenate str (not "int") to str

r = name + str(age)   #type casting we have to do here

print(r)      # Op=> pramod65

g = "Hello"
g+= "India"      # when we use g<space>+ then it through error

print(g)    # op=> HelloIndia

# it is like

gg = "hellooo"

gg = gg + "hellooo"   # we can define this like  gg+= "hellooo"

# Increment and Decrement

p = 5
p-= 1

print(p)   # op+> 4

x = 10
y = ++x   #x+1
print(y)  # op=> 10 | increment like java is not allowed in python for ++












 # Ternary Operator    | will be covered in loop

x = 10
y = 20

a = True

print(not a)    # Op=> False


