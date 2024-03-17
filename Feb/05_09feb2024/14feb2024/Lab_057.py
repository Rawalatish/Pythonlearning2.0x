# Functions
# Block of code - which can executed
# They can return something
# The can't return -> non return

# They have parameters
# They don't parameters / arguments

# Define -> Call

def say_hello():  # | defining part | this is not returning anything because we are not used return here | Non-return type and No Parameter / Argument
    # write the code
    print("hello")


say_hello()  # | calling part | let me execute code which is defined


def say_hello_arg(name):  # No Return Type and with Argument
    # Write the Code
    print("Hello", name)


say_hello_arg("pramod")


# say_hello_arg()       # here if we dont pass the value then we will get the error
##########

def say_hello_args(name, age):  # No Return Type and with multiple  Argument
    # Write the Code
    print("Hello", name, age)


say_hello_args("pramod", 67)
say_hello_args(123, True)
say_hello_args(123, "atish")


def say_hello_arg_default(name="Pramod"):  # No Return Type and with Argument
    # Write the Code
    print("Hello", name)


say_hello_arg_default()  # op= Pramod

# say_hello_arg_default()  | here if we don't pass the value then we get default value i.e "pramod"

say_hello_arg_default("Patil")  # op = patil | if we pass the value then it will replace the default value


################

def sum_number_argument_ret(a, b):  # Return with argument
    return a + b                    # jo return mai logic define kiya hai wo output mai aayega


result = sum_number_argument_ret(3, 4)
result2 = sum_number_argument_ret("Amit", "Pramod")
result3 = sum_number_argument_ret(a=10, b=90)
# result4 = sum_number_argument_ret(a="Amit", b=90)     | this will give error int+str
print(result)
print(result2)
print(result3)
