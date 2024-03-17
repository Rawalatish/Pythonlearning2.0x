# Tuple - It is Collection of items like a list

# List - Collection of items, In list we can change the list and print it, because List is mutable in nature

my_list = [1, 2, 3, 4, 5]
my_list[0] = 21

print(my_list)          # Op= [21, 2, 3, 4, 5]

print(type(my_list))       # <class 'list'>


# Tuple - It is Collection of items. and it is defined with () round bracket
#       - It is immutable in nature, we can't change the value of Tuple
#       - In that we can convert List [] into tuple () but value can't be change

my_tuple = (1, 2, 3, 4, 5)

#my_tuple[0] = 21  # TypeError: 'tuple'

print(my_tuple)

print(type(my_tuple))                             # <class 'tuple'>

print(len(my_tuple))                              # op = 5 | length

#       - In that we can convert List [] into tuple () but value can't be change

new_tup = tuple(my_list)
print(new_tup)