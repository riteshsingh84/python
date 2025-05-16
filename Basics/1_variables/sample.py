"""
This is the sample program to work with variables in python.
"""

person_name = "Ritesh Singh" # String variable
person_age = 23 # Integer variable
person_height = 25.99 # Float variable
person_married = True  # Boolean variable. True or False
person_income = None # None variable. None is a special constant that represents the absence of a value or a null value. No Value is assigned to this variable.
# Above naming convention is called snake_case

# Printing the variables
print("Person Name: ", person_name)
print("Person Age: ", person_age)
print("Person Height: ", person_height)
print("Person Married: ", person_married)
print("Person Income: ", person_income)

# Printing the type of variables
print("Type of Person Name: ", type(person_name))
print("Type of Person Age: ", type(person_age))
print("Type of Person Height: ", type(person_height))
print("Type of Person Married: ", type(person_married))
print("Type of Person Income: ", type(person_income))

x = 4 + 5j # Complex number
print("Type of x: ", type(x))
print(x)
