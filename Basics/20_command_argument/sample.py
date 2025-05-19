"""
This script demonstrates the use of the argparse module to process command-line arguments for basic arithmetic operations.
Positional Arguments:
    number1 (int): The first integer operand.
    number2 (int): The second integer operand.
Optional Arguments:
    --operation (str): The arithmetic operation to perform. Choices are 'add', 'subtract', 'multiply', or 'division'. Defaults to 'add'.
The script prints the input numbers, the selected operation, and the result of the operation.
"""

import argparse

# Create the parser
# The argparse module provides a way to handle command-line arguments in Python scripts.
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="This is sample program to process some integers as an commandline argument.")   
    parser.add_argument("number1", help="first number") # positional argument
    parser.add_argument("number2", type=int, help="second number") # positional argument
    # optional argument with default value
    parser.add_argument("--operation",help="operation: add,subtract,multiply,division", choices=["add", "subtract", "multiply", "division"], default="add") 
    
    args = parser.parse_args() # parse the arguments

    number1 = int(args.number1)
    number2 = args.number2
    operation = args.operation #
    result = None

    print ("number1",number1)
    print ("number2",number2)
    print ("operation",operation)

    if operation == "add":
        result = number1 + number2
    elif operation == "subtract":
        result = number1 - number2
    elif operation == "multiply":
        result = number1 * number2
    elif operation == "division":
        if number2 == 0:
            print("Error: Division by zero is not allowed.")
            result = None
        else:
            result = number1 / number2
    else:
        print ("Invalid operation")        

    print ("Result",result)