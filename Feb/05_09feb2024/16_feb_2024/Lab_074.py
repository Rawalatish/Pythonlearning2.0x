# Filter
# It can filter the items from the list based on the logic
# return less number of items

number = [1, 2, 3, 4, 5, 6]

def even(num):
    return num % 2 == 0                    # print even number and,  == 1 print odd

#  or we can use lambda function instead of def function
# even_lambda = lambda num: num % 2 == 0

even_numbers = filter(even, number)
print(list(even_numbers))

# even_no = filter(lambda x : x%2 == 0,number)
# print(list(even_no))

