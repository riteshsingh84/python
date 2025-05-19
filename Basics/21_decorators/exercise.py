# 1. Create a decorator function to check that the argument passed to the function factorial is a non-negative integer:
# The check_int_raise decorator is used to validate the input and print error message if there is any error.
def check_positive_int(func):
    def wrapper(number):
        if  type(number) == int and number > 0:
            return func(number)
        else:
            print("Error: Argument must be a positive integer: ",number)
            #raise ValueError("Argument must be a positive integer")
    return wrapper

# The check_int_raise decorator is used to validate the input and raise exception if there is any error.
def check_int_raise(func):
    def wrapper(number):
        if  type(number) == int and number > 0:
            return func(number)
        else:           
            raise ValueError(f"Argument must be a positive integer: {number}")
    return wrapper

# 2. Create a factorial function which finds the factorial of a number.
@check_int_raise
def calc_factorial(number):
    result = 1
    for i in range(1, number+1):
        result *= i
    return result

# 3. Use the decorator to decorate the factorial function to only allow factorial of non-negative integers.
try:
    calc_factorial(1.354) # print error message
except ValueError as e:
    print(e)  # Output: Argument must be a positive integer

try:
    calc_factorial(-1) # print error message
except ValueError as e:
    print(e)  # Output: Argument must be a positive integer

factorial_num = calc_factorial(5)
print(factorial_num)  # Output: 120
