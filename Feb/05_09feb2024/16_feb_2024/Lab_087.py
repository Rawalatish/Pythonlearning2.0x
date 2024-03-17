my_dict = {'a': 1, 'b': 2, 'c': 3, 'a': 95}

print(my_dict)                               # {'a': 95, 'b': 2, 'c': 3}

print(my_dict.get('a'))                      # 95

keys = my_dict.keys()
print(keys)                                  # dict_keys(['a', 'b', 'c'])

values = my_dict.values()
print(values)                                # dict_values([95, 2, 3])

keys_list = list(keys)
print(keys_list)                             # ['a', 'b', 'c']

