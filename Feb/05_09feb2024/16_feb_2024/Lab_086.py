#                                                Dictionary  - it is also used in api automation
# Key and Value
name = "Pramod"                #| it a normal string not a dictionary
# Key -> name

# Value -> "Pramod"

# A dictionary is an unordered collection of data
# in a key-value pair format.
#  Keys can't be duplicate, in that case last key would be kept
#  | Values can be duplicate

my_dict  = {}                            # op = {}
my_dict2 = dict()                        # op = {}
print(my_dict2)
print(type(my_dict))                     # <class 'dict'>
print(type(my_dict2))                    # <class 'dict'>

#  Dict eg with curly braces
phone_book = {"Batman": 987654321, "Superman": 1234567890, "Wonder": 97876545}
print(len(phone_book))                   # 3
print(phone_book["Batman"])              # 987654321

#  Dict eg with round braces
phone_book2 = dict(Batman=123, Cersei=342, GB=323)
print(phone_book2)

print(phone_book2['GB'])                         # 323
print(phone_book2["GB"])                         # 323
print(phone_book2.get('GB'))                     # 323
print(phone_book2.get("GB"))                     # 323

pramod_details = dict(name="Pramod", age=34, isMale=True, Address="KA")

# when we dont use dict funtion then we have to use curly braces and also we have to define the key value in double quate ""

pramod_details2 = {"name": "Pramod", "90": 34.34, "isMale": True, "Address": "KA"}
print(pramod_details2.get("90"))


my_dict = {'a': 1, 'b': 2, 'c': 3, 'a': 95}       # Keys can't be duplicate, in that case last key would be kept
                                                  #| Values can be duplicate
print(len(my_dict))                               # 3
print(my_dict)                                    # {'a': 95, 'b': 2, 'c': 3}

