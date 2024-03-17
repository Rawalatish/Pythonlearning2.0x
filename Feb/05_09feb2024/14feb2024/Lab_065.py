# List
#  - it a collection of items (Duplicate items are allowed)

my_list = [1, 2, 3]     #(0,1,2)
my_list2 = [1, True, "Pramod", 12.34]   # list can have  multiple data types

#Indexing
print("Element at index 0:", my_list[0])    # list can have indexing

# Changing an element in list
my_list[1] = 20                                     # we can change the value of list
print("List after changing element at index 1:", my_list)


# append()                        # append means In the end, add this,,,,
my_list.append(4)
print("List after appending:", my_list)        # o/p [1, 2, 3, 4]

# extend()                        # add a new list into existing list
my_list.extend([5, 6])
print("List after extending:", my_list)      # O/p = [1, 20, 3, 4, 5, 6]

# insert()
my_list.insert(1, 'a')        # insert the object value in the list at index number
print("List after inserting 'a' at index 1:", my_list)  #List after inserting 'a' at index 1: [1, 'a', 20, 3, 4, 5, 6]
                                                        # at here we inserted 'a' at 1 indexing position

# remove()
my_list.remove('a')
print("List after removing 'a':", my_list)    # [1, 20, 3, 4, 5, 6]

# copy()                                      # copying the existing list
my_copy_list = my_list.copy()
print(my_copy_list)

# clear()

# my_list.clear()                          # commenting this becasue list get cleared and getting error next list e.g
print("Initial list:", my_list)           # O/p = []       # Initially existing list will get cleared
print(my_copy_list)                        # but copy of list will not get cleared

#indexing

print("Index of 3 in the list:", my_list.index(3))    # O/p = Index of 3 in the list: 2

# sort()
my_copy_list.sort()
print(my_copy_list)                             # O/p [1, 3, 4, 5, 6, 20]   | list is sorted in ascending order

# reverse()
my_copy_list.reverse()
print(my_copy_list)                              # O/p [20, 6, 5, 4, 3, 1]   | in descending order | reverse the list


print(my_copy_list[0])
print(my_copy_list[1])
print(my_copy_list[2])
print(my_copy_list[3])




