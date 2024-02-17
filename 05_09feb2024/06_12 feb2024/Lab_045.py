# pass --> basically means Skip the code

for i in range(10):     # here in range we did not define 0 or 1, 2...| if we dont define it is by default zero 0
    if i == 5:
        pass        # in this  5 will not  be printed if i == 5  and else condition apply and we use pass but if we use break then upto 4 will be printed
    else:
        print(i)    # o/p 0 to 9 expect "5"
