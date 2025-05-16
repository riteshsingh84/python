# Python List vs Set vs Dict Comprehension

## List
List comprehension is a concise way to create lists in Python using a single line of code. It’s often more readable and efficient than using a traditional for loop.

    1. Ordered collection of items
    2. Allows duplicates
    3. Mutable (can be changed after creation)
    4. Items are accessed by index
    5. Initialize with []
### Basic Syntax
    [expression for item in iterable if condition]

* **expression:** the value to put in the list
* **item:** the variable representing each element * in the iterable
* **iterable:** a sequence (like a list, range, etc.)
* **condition (optional):** a filter to include only certain items

### Example:
    1. Using list comprehension to create a new list with even numbers

    even_numbers = [num for num in numbers if num % 2 == 0]
    print("Even numbers using list comprehension:", even_numbers)

## Set
Set comprehension in Python is similar to list comprehension, but it creates a set instead of a list. The syntax is almost the same, except you use curly braces {} instead of square brackets [].

    1. Unordered collection of unique items
    2. No duplicates allowed
    3. Mutable, but items must be immutable (e.g., no lists inside sets)
    4. No indexing (you can’t access items by 
    position)
    5. Initialize with {}
  
### Basic Syntax
    {expression for item in iterable if condition}

* Creates a set by evaluating the expression for each item in the iterable.
* Automatically removes duplicates (since sets only store unique values).

### Example:
    1. Using set comprehension to create a new set with unique numbers
    duplicate_numbers = [1,2,4,3,5,6,7,8,9,10,1,2,3,4,5]
    unique_numbers = {num for num in duplicate_numbers} 
    unique_numbers_set = set(duplicate_numbers) #alternative way to create a set
    print("Unique numbers using set comprehension:", unique_numbers, unique_numbers_set)

## Dictionary (dict)

Dictionary comprehension is a concise way to create dictionaries in Python using a single line of code. It’s similar to list and set comprehensions, but it builds key-value pairs.

    1. Collection of key-value pairs
    2. Keys must be unique and immutable
    3. Values can be any type
    4. Mutable
    5. Initialize with {}

### Basic Syntax
    {key_expression: value_expression for item in iterable if condition}

* **key_expression:** what you want to use as the key
* **value_expression:** what you want to use as the value
* **iterable:** a sequence to loop over
* **condition (optional):** filter to include only certain items

### Example:
    original = {"a": 1, "b": 2, "c": 3}
    swapped = {v: k for k, v in original.items()}
    print(swapped)  # Output: {1: 'a', 2: 'b', 3: 'c'}


## Exercise

1. Create a Dictionary which contains the Binary values mapping with numbers found in the below integer and binary and save it in binary_dict.
Example :

        integer = [0, 1, 2, 3, 4]
        binary = ["0", "1", "10", "11", "100"]
        binary_dict = {0:"0", 1:"1", 2:"10", 3: "11", 4:"100"}

2. Create a List which contains additive inverse of a given integer list. An additive inverse a for an integer i is a number such that:
a + i = 0
Example:

        integer = [1, -1, 2, 3, 5, 0, -7]
        additive_inverse = [-1, 1, -2, -3, -5, 0, 7]

3. Create a set which only contains unique sqaures from a given a integer list.

        integer = [1, -1, 2, -2, 3, -3]
        sq_set = {1, 4, 9}
   
   [Solution](https://github.com/riteshsingh84/python/tree/main/Basics/18_list_set_dict/exercise.py)
