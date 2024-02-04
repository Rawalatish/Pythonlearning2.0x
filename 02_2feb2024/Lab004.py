# $ = $ as variable is not allowed in python.
# 123 = numbering as variable is not allowed in python
# _123 = '_123' numbering staring with underscore is allowed.

import keyword

# click on the keyword + press Ctrl+ click on the keyword to see all keywords list
# or run below command to see keyword list in console
print(keyword.kwlist)

# we can't use keywords as a variable

print("i", "love", "my", "India")
print("i", "love", "my", "India", sep="_")  # seperator
print("i", "love", "my", "India", end="%")
print("i", "love", "my", "Indiaaaaa")

