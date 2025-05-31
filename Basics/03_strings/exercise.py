
'''1. Create 3 variables to store street, city and country, now create address variable to store entire address.
 Use two ways of creating this variable, one using + operator and the other using f-string.
Now Print the address in such a way that the street, city and country prints in a separate line
'''
print("""1. Create 3 variables to store street, city and country, now create address variable to store entire address.
 Use two ways of creating this variable, one using + operator and the other using f-string.
Now Print the address in such a way that the street, city and country prints in a separate line.\n""")  # print statement for clarity

street ="Berkwerkstrasse 34"  # variable to store street address
city = "Sargans"    # variable to store city name
country = "Switzerland" # variable to store country name

my_address = street +"\n"+ city +"\n" + country     # using + operator to create address variable

print("Address using + operator:\n" + my_address)  

print(f"Address using f-string:\n{street} \n{city}\n{country}")  # using f-string to create address variable

'''
2. Create a variable to store the string "Earth revolves around the sun"
Print "revolves" using slice operator
Print "sun" using negative index
'''
print("""\n2. Create a variable to store the string "Earth revolves around the sun"
Print "revolves" using slice operator
Print "sun" using negative index\n""")  # print statement for clarity

text = "Earth revolves around the sun"  # variable to store the string

print('Print "revolves" using slice operator: ' + text[6:14])  # using slice operator to print "revolves"     

print('Print "sun" using negative index: ' + text[-3::]) # using negative index to print "sun"



'''
3. Create two variables to store how many fruits and vegetables you eat in a day.
 Now Print "I eat x veggies and y fruits daily" where x and y presents vegetables and fruits that you eat everyday.
 Use python f string for this.
'''
print("""\n3. Create two variables to store how many fruits and vegetables you eat in a day.
 Now Print "I eat x veggies and y fruits daily" where x and y presents vegetables and fruits that you eat everyday.
 Use python f string for this.\n""")  # print statement for clarity

fruits = "Apple,Grapes,Banana,Kiwi,Peers,Mango"  # variable to store fruits as a comma-separated string
vegetables = "Potato,Carrot,Cabbage,Spinach,Onion,Tomato"

print(f"I eat {len(vegetables.split(','))} veggies ({vegetables}) and {len(fruits.split(','))} fruits ({fruits}) daily")  # using f-string to print the number of veggies and fruits eaten daily


'''
4. I have a string variable called s='maine 200 banana khaye'.
This of course is a wrong statement, the correct statement is 'maine 10 samosa khaye'.
Replace incorrect words in original strong with new ones and print the new string. Also try to do this in one line.
'''
print("""\n4. I have a string variable called s='maine 200 banana khaye'.
This of course is a wrong statement, the correct statement is 'maine 10 samosa khaye'.
Replace incorrect words in original strong with new ones and print the new string. Also try to do this in one line.\n""")  # print statement for clarity

s='maine 200 banana khaye' # original string variable
print(s)    # printing the original string
s = s.replace("200","10").replace("banana","samosa")        # replacing incorrect words with correct ones in one line
print(s)

