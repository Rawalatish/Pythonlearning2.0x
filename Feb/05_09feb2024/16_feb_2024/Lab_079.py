# Multiple assignments in tuple

x = 10
a, b = 23, 34
q, w, e = (45, 56, 78)                      # Multiple assignments in tuple

# Nested Tuples
hero1 = ("Batman", "Bruce Wayne")
hero2 = ("Wonder Woman", "Diana Prince")
awesome_team = (hero1, hero2)                         # Concatenation of 2 tuple is not happening here because tuple in tuple refer lab079 for Concatenation of 2 tuple
                                                      # op = (('Batman', 'Bruce Wayne'), ('Wonder Woman', 'Diana Prince'))

print(awesome_team)                                   # op = (('Batman', 'Bruce Wayne'), ('Wonder Woman', 'Diana Prince'))

print(awesome_team[0])                                # op = ('Batman', 'Bruce Wayne')

print(awesome_team[0][1])                             # op = Bruce Wayne

print(awesome_team[1][1])                             # op = Diana Prince

# Search in Tuple
cities = ("London", "Paris", "Los Angeles", "Tokyo")
print("Paris" in cities)                          # TRUE
print("Moscow" in cities)                         # FALSE
print("Kolhapur" in cities)                       # FALSE
print("Pune" in hero1)                            # FALSE
