from collections import OrderedDict
od =  OrderedDict()
od['a'] = 45
od['e'] = 7                                                  # 07 is not accepted
od['c'] = 78
od['b'] = 97
od['d'] = 31
print(od)                                       # OrderedDict({'a': 45, 'e': 7, 'c': 78, 'b': 97, 'd': 31})

# Dict - It will not keep the Order of insertion
# OrderedDict - It will keep the order of insertion