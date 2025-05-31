# Python List 
In Python, a list is a built-in data type used to store multiple items in a single variable. 

## 🧾 List
List provides a way to 

    1. Ordered collection of items
    2. Allows duplicates
    3. Mutable (can be changed after creation)
    4. Items are accessed by index
    5. List can contain elements of different data types
    6. You create a list using square brackets []

### ✅ Example:
    fruits = ["apple", "banana", "cherry", "apple"]
    print(fruits[1])  # Output: banana

## 🔧 Basic Syntax

### 1. Creating a List

You create a list using square brackets **[]**.

    fruits = ["apple", "banana", "cherry"]
    numbers = [1, 2, 3, 4, 5]
    mixed = [1, "hello", 3.14, True]

### 2. Accessing Elements

Use indexing to access elements (starting from 0):

    fruits = ["apple", "banana", "cherry"] 
    print(fruits[0])     # 'apple'
    print(fruits[-1])    # 'cherry' (last item)


### 3. Modifying Elements

Lists are mutable, so you can change elements:
    
    fruits[1] = "blueberry"


### 4. List Slicing

    numbers = [0, 1, 2, 3, 4, 5]

    print(numbers[1:4])   # [1, 2, 3]
    print(numbers[:3])    # [0, 1, 2]
    print(numbers[::2])   # [0, 2, 4]


### 5. Looping Through a List

    fruits = ["apple", "banana", "cherry"] 
    for fruit in fruits:
        print(fruit)

### 6. Sorting  a List
The .sort() method in Python is used to sort the elements of a list in place, meaning it changes the original list. By default, it sorts in ascending order, but you can also sort in descending order or use a custom key.

    words = ["banana", "apple", "cherry"]
    words.sort()
    print(words)  # Output: ['apple', 'banana', 'cherry']

**Custom Sorting with key**

Use the reverse=True argument:

    numbers = [5, 2, 9, 1, 7]
    numbers.sort(reverse=True)
    print(numbers)  # Output: [9, 7, 5, 2, 1]

**Descending Order**

You can sort based on a custom rule using the key parameter.

Example: Sort by length of words

    numbers = [5, 2, 9, 1, 7]
    numbers.sort(reverse=True)
    print(numbers)  # Output: [9, 7, 5, 2, 1]

 **Important Notes**

* .sort() modifies the original list and returns None.
* If you want to keep the original list unchanged, use the built-in sorted() function

        sorted_list = sorted(numbers)


### 7. Nested Lists

Lists can contain other lists:

    matrix = [[1, 2], [3, 4]]
    print(matrix[0][1])  # 2


## 🔧 List Operations
### 1. Add items:
    fruits.append("orange")         # Add to end
    fruits.insert(1, "kiwi")        # Insert at index

### 2. Remove items:
    fruits.remove("apple")          # Remove by value
    fruits.pop()                    # Remove last item
    del fruits[0]                   # Delete by index

### 3. Check membership:
    "banana" in fruits              # True or False

## 📚 Useful Functions

* **len** – Get number of items in list
* **sort** – Sorting list item. .sort() modifies the original list and returns None.
* **sorted** – If you want to keep the original list unchanged, use the built-in sorted() function.
* **reverse** – reverse listing
* **clear** – Empty the list
* **insert(index,item)** – Insert item in list at given index
* **remove** – Remove item from list by value.
* **pop** – Remove the last item from list.
* **del list[index]** – Delete item from list by index.
* **len** – Get the length of the string.

## 🧠 Exercise

1. Let us say your expense for every month are listed below,
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

2. You have a list of your favourite marvel super heros.
```
heros=['spider man','thor','hulk','iron man','captain america']
```

Using this find out,

    1. Length of the list
    2. Add 'black panther' at the end of this list
    3. You realize that you need to add 'black panther' after 'hulk',
       so remove it from the list first and then add it after 'hulk'
    4. Now you don't like thor and hulk because they get angry easily :)
       So you want to remove thor and hulk from list and replace them with doctor strange (because he is cool).
       Do that with one line of code.
    5. Sort the heros list in alphabetical order (Hint. Use dir() functions to list down all functions available in list)

   
   [Solution](https://github.com/riteshsingh84/python/tree/main/Basics/04_lists/exercise.py)
