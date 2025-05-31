# Python Numbers

IIn Python, a string is a sequence of characters enclosed in either single quotes ('...') or double quotes ("..."). Strings are used to represent text and are one of the most commonly used data types in Python. 

## 🔢 Rules and key characteristics
### 1. Definition and Syntax (string)
* Strings are defined using single quotes ('...') or double quotes ("...").
* Triple quotes ('''...''' or """...""") are used for **multi-line strings**.

        s1 = 'Hello'
        s2 = "World"
        s3 = '''This is
        a multi-line
        string.'''


### 2. Immutability

* Strings in Python are immutable, meaning once created, their contents cannot be changed.

Examples: 

        text = "hello"
        text[0] = 'H'  # ❌ This will raise an error


### 3. Indexing and Slicing

* Strings support indexing (positive and negative) and slicing.

Examples: 

    word = "Python"
    print(word[0])    # 'P'
    print(word[-1])   # 'n'
    print(word[1:4])  # 'yth'

### 4. Concatenation and Repetition

* Use + to concatenate and * to repeat strings.

Examples: 

    "Py" + "thon"     # 'Python'
    "ha" * 3          # 'hahaha'

### 5. Escape Characters

* Use \ to escape special characters:

Examples: 

    quote = "He said, \"Hello!\""
    newline = "Line1\nLine2"


### 6. String Formatting

* Python supports several ways to format strings:

Examples: 

    name = "Ritesh"
    f"Hello, {name}!"              # f-string
    "Hello, {}!".format(name)      # format method
    "Hello, %s!" % name            # old-style formatting


### 6. Membership and Iteration

* You can check if a substring exists and iterate over strings:

Examples: 

    "th" in "Python"     # True
    for char in "Hi":    # Iterates over 'H' and 'i'
        print(char)


## 📚 Useful Functions

* **upper** – Convert string to upper case
* **lower** – Convert string to lower case
* **title** – Convert string to title case
* **isalnum** – Check string is alpha numeric or not
* **replace** – Find and replace some string within string
* **startswith** – Check if string is starting with some string or not.
* **len** – Get the length of the string.

Examples:

    "hello".upper()       # 'HELLO'
    "HELLO".lower()       # 'hello'
    "hello world".title() # 'Hello World'
    "abc123".isalnum()    # True
    "Python".replace("Py", "My")  # 'Mython'  
    "Python".startswith("Py")  # True
    len("Python")  # 6


## 🧠 Exercise

1. Create 3 variables to store street, city and country, now create address variable to store entire address. Use two ways of creating this variable, one using + operator and the other using f-string. Now Print the address in such a way that the street, city and country prints in a separate line

2. Create a variable to store the string "Earth revolves around the sun"
Print "revolves" using slice operator
Print "sun" using negative index

3. Create two variables to store how many fruits and vegetables you eat in a day. Now Print "I eat x veggies and y fruits daily" where x and y presents vegetables and fruits that you eat everyday. Use python f string for this.

4. I have a string variable called s='maine 200 banana khaye'. This of course is a wrong statement, the correct statement is 'maine 10 samosa khaye'. Replace incorrect words in original strong with new ones and print the new string. Also try to do this in one line.
   
   [Solution](https://github.com/riteshsingh84/python/tree/main/Basics/03_strings/exercise.py)
