# Python Sets and Frozen Sets

## 🧮 Set
A Set is:

    1. Unordered collection of unique items
    2. No duplicates allowed. Automatically removes duplicates.
    3. Mutable (You can add or remove elements), but items must be immutable (e.g., no lists inside sets)
    4. No indexing (you can’t access items by position)
  
### 🔧 Basic Syntax
    {comma separated items}

### ✅ Example:
   colors = {"red", "green", "blue", "red"}
    print(colors)  # Output: {'red', 'green', 'blue'} — duplicates removed

## 🔧 Common Methods:
* add(), remove(), discard()
* union(), intersection(), difference()

## 🧊 Frozenset

A frozenset is:

    1. Immutable: Cannot be changed after creation
    2. Still unordered and unique
    3. Useful as a dictionary key or in other sets (because it's hashable)  

### Basic Syntax
    frozenset([comma separated items])

### Example:
    my_frozenset = frozenset([1, 2, 3, 2])
    print(my_frozenset)  # Output: frozenset({1, 2, 3})


## Exercise

1. Create any set anf try to use frozenset(setname)

2. Find the elements in a given set that are not in another set
Example:

        set1 = {1,2,3,4,5}
        set2 = {4,5,6,7,8}

        Difference between set1 and set2 is {1,2,3}
   
   [Solution](https://github.com/riteshsingh84/python/tree/main/Basics/19_sets_frozensets/exercise.py)
