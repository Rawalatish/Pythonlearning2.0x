# Map()  | it is a function

def sq_of_number(num):
    return num ** 2                       # this gives the square of number


result = sq_of_number(10)
print(result)

numbers = [1, 2, 3, 4, 5]

sq_num = map(sq_of_number, numbers)    # Op is in Map so we have to convert this into list

print("mapppp",sq_num)

sq_num1 = list(map(sq_of_number, numbers))

print("after converting",sq_num1)    # op= [1, 4, 9, 16, 25]



# Map() -
# 1. Takes Each item from the list then
# 2. execute the function on it.
# 3. Return same number of elements ( list)

