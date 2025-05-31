first_name = "Ritesh" # string variable, storing first name
last_name = "Singh" # string variable, storing last name

full_name = first_name + " " + last_name # concatenating first and last name

print("Hello, " + full_name + "!") # printing a greeting message


# Print the length of the full name
print("Length of full name:", len(full_name)) # using len() function to get the length of the full name

# Print the first character of the full name
print("First character of full name:", full_name[0]) # accessing the first character using indexing

# Print the last character of the full name
print("Last character of full name:", full_name[-1]) # accessing the last character using negative indexing

# Print the full name in reverse order
print("Full name in reverse order:", full_name[::-1]) # reversing the full name using slicing

# First 6 characters of the full name
print("First 6 characters of full name:", full_name[:6]) # slicing the first 6 characters

# Print the last 6 characters of the full name
print("Last 6 characters of full name:", full_name[-6:]) # slicing the last 6 characters using negative indexing

# print the range of characters from index 2 to 5
print("Characters from index 2 to 5:", full_name[2:6]) # slicing characters from index 2 to 5

# print first name and last name separately from the full name
print("First name:", full_name.split()[0]) # splitting the full name and printing the first name
print("Last name:", full_name.split()[1]) # splitting the full name and printing the last name

# Check full name starts with a specific letter
print("Does the full name start with 'R'? :", full_name.startswith("R")) # checking if the full name starts with 'R'

# Check full name ends with a specific letter
print("Does the full name end with 'h'? :", full_name.endswith("h")) # checking if the full name ends with 'h'

# Replace a part of the full name
print("Full name after replacing 'Ritesh' with 'Raj':", full_name.replace("Ritesh", "Raj")) # replacing 'Ritesh' with 'Raj'

# Check if the full name contains a specific substring
print("Does the full name contain 'Singh'? :", "Singh" in full_name) # checking if 'Singh' is in the full name

# Print the full name in uppercase
print("Full name in uppercase:", full_name.upper()) # converting the full name to uppercase
# Print the full name in lowercase
print("Full name in lowercase:", full_name.lower()) # converting the full name to lowercase
# Print the full name with the first letter of each word capitalized
print("Full name with capitalized words:", full_name.title()) # capitalizing the first letter of each word

my_address = """BerkwerkStrasse 12
Sargans
7230
Switzerland""" # multi-line string variable, storing address
# Print the address 
print("My address:\n" + my_address) # printing the address with a newline character

# print my address with full name
print(f"My full address:\n{first_name} {last_name}\n{my_address}" ) # printing the full address with the full name


