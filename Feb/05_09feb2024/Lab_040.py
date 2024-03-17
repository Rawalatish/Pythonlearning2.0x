for x in range(5):
    print(x)

print("=====")

for x in range(1, 5, 2):
    print(x)

# But what is the range = it is the function that will give you multiple value  | range vs range()

a = range(5)
print(a)  # Op >  range(0, 5)

a2 = list(range(5))
print(a2)  # OP > [0, 1, 2, 3, 4]
