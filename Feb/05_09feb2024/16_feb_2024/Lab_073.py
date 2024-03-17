import math


def sq_rt(num):
    return math.sqrt(num)                  #sq. root by of any numer using math
    # return math.cbrt(num)                # this is for cube root


# list, set, tuple, dictionary            # when we have multiple item like this then we use map

my_list = [16, 34, 54]
sq_list = list(map(sq_rt, my_list))              # sq. root of list by using map
print(sq_list)



