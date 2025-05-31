print("\n Exercise 1: ") # printing the title of the exercise
'''1. Let us say your expense for every month are listed below,
    1. January -  2200
    2. February - 2350
    3. March - 2600
    4. April - 2130
    5. May - 2190

Create a list to store these monthly expenses and using that find out,

    1. In Feb, how many dollars you spent extra compare to January?
    2. Find out your total expense in first quarter (first three months) of the year.
    3. Find out if you spent exactly 2000 dollars in any month
    4. June month just finished and your expense is 1980 dollar. Add this item to our monthly expense list
    5. You returned an item that you bought in a month of April and
    got a refund of 200$. Make a correction to your monthly expense list
    based on this
'''

my_monthly_expenses = [2200,2350,2600,2130,2190] # list to store monthly expenses
print("Monthly expenses for the first five months of the year:", my_monthly_expenses) # printing the monthly expenses list

# 1. In Feb, how many dollars you spent extra compare to January?
exp_diff_jan_feb = my_monthly_expenses[1] - my_monthly_expenses[0] # difference in expenses between February and January

print ("1. In Feb, how many dollars you spent extra compare to January?",exp_diff_jan_feb) # printing the difference in expenses between February and January

# 2. Find out your total expense in first quarter (first three months) of the year.
first_quarter_exp = my_monthly_expenses[0] + my_monthly_expenses[1] + my_monthly_expenses[2]
print ("2. Find out your total expense in first quarter (first three months) of the year.",first_quarter_exp) # printing the total expense in first quarter (first three months) of the year

# 3. Find out if you spent exactly 2000 dollars in any month
print ("3. Find out if you spent exactly 2000 dollars in any month.",2000 in my_monthly_expenses) # checking if 2000 dollars is in the monthly expenses list

# 4. June month just finished and your expense is 1980 dollar. Add this item to our monthly expense list
my_monthly_expenses.append(1980) # adding June month expense to the monthly expenses list
print("Updated list after adding June month expenses",my_monthly_expenses)

# 5. You returned an item that you bought in a month of April and
#    got a refund of 200$. Make a correction to your monthly expense list
#    based on this
my_monthly_expenses[3] = my_monthly_expenses[3] - 200 # adjusting April month expense by subtracting the refund amount
print("Updated list after adjusting refund in April month expenses",my_monthly_expenses)


print("\n Exercise 2\n ") # printing the title of the exercise

'''2. You have a list of your favorite marvel super heroes.

heroes=['spider man','thor','hulk','iron man','captain america']

Using this find out,

    1. Length of the list
    2. Add 'black panther' at the end of this list
    3. You realize that you need to add 'black panther' after 'hulk',
       so remove it from the list first and then add it after 'hulk'
    4. Now you don't like thor and hulk because they get angry easily :)
       So you want to remove thor and hulk from list and replace them with doctor strange (because he is cool).
       Do that with one line of code.
    5. Sort the heroes list in alphabetical order (Hint. Use dir() functions to list down all functions available in list)
'''


# list variable, storing favorite marvel super heroes
heroes=['spider man','thor','hulk','iron man','captain america'] 
print("Printing the list of favorite marvel super heroes:",heroes) # printing the list of favorite marvel super heroes

# 1. Length of the list
print("Length of the list",len(heroes))

# 2. Add 'black panther' at the end of this list
heroes.append("black panther") # adding 'black panther' at the end of the list
print("Printing the list after adding 'black panther'",heroes) # printing the list after adding 'black panther'

# 3. You realize that you need to add 'black panther' after 'hulk',
#   so remove it from the list first and then add it after 'hulk'
heroes.pop() # removing 'black panther' from the end of the list
heroes.insert(3,'black panther') # adding 'black panther' after 'hulk'
print("Printing the list after adding 'black panther' after 'hulk'",heroes) # printing the list after adding 'black panther' after 'hulk'

# 4. Now you don't like thor and hulk because they get angry easily :)
#       So you want to remove thor and hulk from list and replace them with doctor strange (because he is cool).
# Do that with one line of code.

heroes.remove("thor") # removing 'thor' from the list
heroes.remove("hulk") # removing 'hulk' from the list
heroes.append("doctor strange") # adding 'doctor strange' to the end of the list

print("Printing the list after removing 'thor' and 'hulk' and adding 'doctor strange'",heroes) #   printing the list after removing 'thor' and 'hulk' and adding 'doctor strange'

# 5. Sort the heroes list in alphabetical order 
heroes.sort() # sorting the heroes list in alphabetical order
print("Printing the heroes list after sorting in alphabetical order",heroes) # printing the heroes list after sorting in alphabetical order