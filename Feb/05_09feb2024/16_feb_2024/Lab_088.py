my_dict = {'a': 1, 'b': 2}
val = my_dict.pop('a')                # pop - remove the key and give those key value
print(val)                            # 1            | Here 'a' is removed and 1 gives in op


knights = {'gallahad': 'the pure', 'robin': 'the brave'}
print(len(knights))

for k,v in knights.items():                  # k represent key and v represent value
    print(k," - ", v)                        # gallahad  -  the pure
                                             # robin  -  the brave