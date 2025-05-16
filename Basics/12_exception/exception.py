"""
This is the sample program to handle exception in python
"""

# Take the first number as user input
x = input ("Enter number 1: ")
# Take the second number as user input
y = input ("Enter number 2: ")
# Initialize the number with none, otherwise during the print it may give error
z = None

try:

    # Write your all codes inside try and except block. If something went wrong during code execution it will goes to respective except block
    z = int(x) / int(y) # User input always comes in stirng, so converting into integer

except ZeroDivisionError as e: # Handled the Zero division exception
    print("Division with 0 is not possible.")
except Exception as e: # Handled the any other exception
    print("There is some error occurred: ",e)

print("Division is: ", z)