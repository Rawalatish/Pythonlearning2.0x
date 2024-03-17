# Tuple - e.g

tuple3 = tuple(["Pramod", "Lucky"])            # List can be converted into tuple
print(tuple3)                                 # op ('Pramod', 'Lucky')
print(tuple3[1])                             # op = Lucky

hero1 = ("Batman", "Bruce Wayne")
hero2 = ("Wonder Woman", "Diana Prince")

awesome_team = hero1 + hero2                   # Concatenation of 2 tuple

print(awesome_team)                            # op = ('Batman', 'Bruce Wayne', 'Wonder Woman', 'Diana Prince')
print(list(awesome_team))                      # op = ['Batman', 'Bruce Wayne', 'Wonder Woman', 'Diana Prince']

# Convert to List  - We can convert tuple into List

my_tuple = (1, 2, 3, 4, 5)
print(list(my_tuple))                           #op = [1, 2, 3, 4, 5]

