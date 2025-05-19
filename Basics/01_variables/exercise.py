"""
1. create a variable called break and assign it a value 5. See what happens and find out the reason behind the behavior that you see.
"""
# break = 5 break is a key word in python, so can not use as variable name

"""
2. Create two variables. One to store your birth year and another one to store current year. Now calculate your age using these two variables
"""
from datetime import datetime
birth_year = 1984
current_year = datetime.now().year
age = current_year - birth_year
print("Your age is: ", age)

"""
3. Store your first, middle and last name in three different variables and then print your full name using these variables.
"""
first_name = "Ritesh"
middle_name = "Kumar"
last_name = "Singh"
full_name = f"{first_name} {middle_name} {last_name}" #The f in front of a string stands for "formatted string literal", or simply f-string. It was introduced in Python 3.6 to make string formatting easier and more readable.
print("Your full name is: ", full_name)

"""
4. Answer which of these are invalid variable names: _nation 1record record1 record_one record-one record^one continue

Answer: 1record record-one record^one continue

"""


