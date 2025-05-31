my_groceries = ["Breads", "Fruits", "Veggies", "Pasta", "Milk",]  # list variable, storing grocery items

print("printing the list of grocery items:",my_groceries)  # printing the list of grocery items

# Print the first item in the grocery list
print("First item in the grocery list:", my_groceries[0])  # accessing the first item using indexing

# Print the last item in the grocery list   
print("Last item in the grocery list:", my_groceries[-1])  # accessing the last item using negative indexing

# Print the grocery list in reverse order
print("Grocery list in reverse order:", my_groceries[::-1])  # reversing the grocery list using slicing

# Print the first 3 items in the grocery list
print("First 3 items in the grocery list:", my_groceries[:3])  # slicing the first 3 items  

# Print the last 2 items in the grocery list
print("Last 2 items in the grocery list:", my_groceries[-2:])  # slicing the last 2 items using negative indexing   

# Print the range of items from index 1 to 3    
print("Items from index 1 to 3:", my_groceries[1:4])  # slicing items from index 1 to 3

# Print the grocery list with a specific item replaced
my_groceries[2] = "Vegetables"  # replacing "Veggies" with "Vegetables"
print("Grocery list after replacing 'Veggies' with 'Vegetables':", my_groceries)  # printing the grocery list after replacement

# Add new items to the grocery list
my_groceries.append("Eggs")  # adding "Eggs" to the grocery list
my_groceries.insert(2,"Cheese")  # adding "Cheese" to the grocery list at 3rd position
print("Grocery list after adding new items:", my_groceries)  # printing the grocery list after adding new items

# Check if a specific item is in the grocery list   
print("Is 'Fruits' in the grocery list? :", "Fruits" in my_groceries)  # checking if "Fruits" is in the grocery list

# Print the grocery list in uppercase
print("Grocery list in uppercase:", [item.upper() for item in my_groceries])  # converting each item to uppercase   

#sort the grocery list
my_groceries.sort()
print("Sorted Grocery list :", my_groceries)  

# Sorting the grocery list by length of words
my_groceries.sort(key=len)  
print("Grocery list sorted by length of words:", my_groceries)  # printing the grocery list sorted by length of words

#sort the grocery list in descending order
my_groceries.sort(reverse=True)  
print("Grocery list sorted in descending order:", my_groceries)  # printing the grocery list sorted in descending order

# Merging grocery list with bathroom items
bathroom_items = ["Soap", "Shampoo", "Toothpaste", "Towel", "Toilet Paper"]  # list variable, storing bathroom items

my_all_groceries = my_groceries + bathroom_items  # Merging grocery list with bathroom items with the + operator
print("Grocery list after merging with bathroom items:", my_all_groceries)  # printing the grocery list after merging with bathroom items

my_groceries.extend(bathroom_items)  # Extending grocery list with bathroom items
print("Grocery list after extending with bathroom items:", my_groceries)  # printing the grocery list after extending with bathroom items

