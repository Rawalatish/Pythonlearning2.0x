name = "Dhoni" # 0,1,2,3,4
print(len(name))  # len ~ length is 5 | o/p- 5
print(name[0])     # o/p- D
print(name[3])
# print(name[5])     # o/p IndexError: string index out of range

print(len(name)-1)   # o/p 4

print (name[len(name)-1]) #  o/p i | last char if dhoni | (name[5-1])

# String are Immutability | string are immutable in nature, that can't be changed or modify but we can replace them

g = "Hello"
g = 'India'    # here we replaced the string value

print(g)
g[0] = "p"  # Here we  modify or changed the string value | o/p : TypeError: 'str' object does not support item assignment

