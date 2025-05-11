"""
This is the sample programe to handle exception in python
"""

# Take the first number as user input
x = input ("Enter number 1: ")
# Take the second number as user input
y = input ("Enter number 2: ")
# Initilize the number with none, othwise during the print it may give error
z = None

try:

    # Write your all codes inside try and except block. If somethig went wrong during code execution it will goes to respective except block
    z = int(x) / int(y) # User input always comes in stirng, so converting into integer

except ZeroDivisionError as e: # Handled the Zero division excption
    print("Division with 0 is not possible.")
except Exception as e: # Handled the any other excption
    print("There is some error occured: ",e)

print("Division is: ", z)