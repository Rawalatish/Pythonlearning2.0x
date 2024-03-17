
t = ("TheTestingAcademy", "for", "TheTestingAcademy")

print(set(t))         # When we convert tuple into set, resulting in uniqueness of Tuple is gone | Duplicate is not allowed in set

set1 = {1, 2, 3}
set2 = {7, 8 , 9, 3}

my_set_exe = set1, set2                 # op = ({1, 2, 3}, {8, 9, 3, 7})

print(my_set_exe)

# union

set1 = {1, 2, 3, 4, 5}
set2 = {7, 8 , 9, 4, 5}

my_set = set1.union(set2)
print("union =", my_set)                           #  op = {1, 2, 3, 4, 5, 7, 8, 9}

# intersection

my_set = set1.intersection(set2)                  # Only Common value will get
print("intersection = ", my_set)                  # op = {4, 5}

#  difference

my_set = set1.difference(set2)                    # From set1 remove the duplicates which are present in set2
print("difference", my_set)                       # op = {1, 2, 3}          | here 4,5 are duplicate in set1 and set2

my_set2 = set2.difference(set1)
print(my_set2)                                     # op = {8, 9, 7}


