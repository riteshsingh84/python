numbers=[1,2,3,4,5,7,8,9,10]

# 1. Using list comprehension to create a new list with even numbers
even_numbers = [num for num in numbers if num % 2 == 0]
print("Even numbers using list comprehension:", even_numbers)


# 2. Using list comprehension to create a new list with odd numbers
odd_numbers = [num for num in numbers if num % 2 != 0]
print("Odd numbers using set comprehension:", odd_numbers)

# 3. Using list comprehension to create a new list with squares of numbers
squares_numbers = [num ** 2 for num in numbers]
print("Squares of numbers using dictionary comprehension:", squares_numbers)


# 4. Using set comprehension to create a new set with unique numbers
duplicate_numbers = [1,2,4,3,5,6,7,8,9,10,1,2,3,4,5]
unique_numbers = {num for num in duplicate_numbers} 
unique_numbers_set = set(duplicate_numbers) #alternative way to create a set
print("Unique numbers using set comprehension:", unique_numbers, unique_numbers_set)

# 5. Using dictionary comprehension to create a new dictionary with cities and their continents
cities = ['New York', 'Tokyo', 'Paris', 'London']   
continents = ['North America', 'Asia', 'Europe', 'Europe']
city_continent_dict = {city: continent for city, continent in zip(cities, continents)}     
print("City and continent dictionary using dictionary comprehension:", city_continent_dict)

#6. Using dictionary comprehension to create a new dictionary with Swap keys and values
swap_dict = {v: k for k, v in city_continent_dict.items()}
print("Swapped dictionary using dictionary comprehension:", swap_dict)  
