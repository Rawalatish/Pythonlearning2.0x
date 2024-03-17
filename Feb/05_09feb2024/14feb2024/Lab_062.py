# Factorial program with using the function -  HW

# Reverse a String

str = "Chemical"
rev_str = ""
for c in str:
    rev_str = c + rev_str

print(rev_str)


# Reverse a string by using defining the function

def reverse_string(str):
    rev_str = ""
    for c in str:
        rev_str = c + rev_str
    return rev_str


original_str = input("enter the string\n")
original_str = original_str.lower()
rev_str = reverse_string(original_str)
print(rev_str)

# Palindrome - str = rev_str -> p
if original_str == rev_str:
    print("this string is Palindrome")
else:
    print("not a palindrome")


