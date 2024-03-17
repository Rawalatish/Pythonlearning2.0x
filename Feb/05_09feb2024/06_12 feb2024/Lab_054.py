
# Funtion --> Block of code which will help you to execute some task
# Define the function
# and call that defined function

#non-return function
# Define the function-
def greet():
    print("Hello, how are you?")

result = greet()
print(result)          # O/p = None

# Call the function
greet()    # O/p - Hello, how are you?
greet()
greet()
greet()
print("===========")

for i in range(5):
    greet()
