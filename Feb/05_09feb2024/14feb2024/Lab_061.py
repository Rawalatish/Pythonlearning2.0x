def make_pizza(*toppings, base="Wheat"):
    print(toppings, base)
    for topping in toppings:            #| if i run this code till this line then nothing will be print because its a
                                         # def function area and i have to call this defeine function in calling area
        print(topping)
    return toppings, base            # if we dont use return in that case we will can't assign make_pizza in variable
                                    # and if we do then it will give "None" in Output


swati =  make_pizza("Onion", 'tomato', "sweetcorn", base = "magargitta")
print(swati)


