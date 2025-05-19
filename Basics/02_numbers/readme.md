# Python Numbers

In Python, numbers are a fundamental data type used to represent numeric values. There are several types of numbers in Python, each suited for different kinds of mathematical operations. 

## 🔢 Types of Numbers in Python
### 1. Integers (int)
* Whole numbers, positive or negative, without decimals.
* Examples: 5, -42, 1000000

### 2. Floating Point Numbers (float)

* Numbers with decimal points or in exponential (scientific) notation.
* Examples: 3.14, -0.001, 2.5e3 (which is 2500.0)

### 3. Complex Numbers (complex)

* Numbers with a real and imaginary part.
* Written as a + bj, where a is the real part and b is the imaginary part.
* Example: 3 + 4j
  
## 🧮 Basic Operations
You can perform arithmetic operations with numbers:

    a = 10
    b = 3

    print(a + b)   # Addition: 13
    print(a - b)   # Subtraction: 7
    print(a * b)   # Multiplication: 30
    print(a / b)   # Division: 3.333...
    print(a // b)  # Floor Division: 3
    print(a % b)   # Modulus: 1
    print(a ** b)  # Exponentiation: 1000

## 🔄 Type Conversion
You can convert between number types:

    int(3.7)       # 3
    float(5)       # 5.0
    complex(2)     # (2+0j)

## 📚 Useful Functions

* **abs(x)** – Absolute value
* **round(x, n)** – Round to n decimal places
* **pow(x, y)** – Equivalent to x ** y
* **divmod(x, y)** – Returns a tuple (x // y, x % y)

## 🧠 Exercise

1. You have a football field that is 92 meter long and 48.8 meter wide. Find out total area using python and print it.
2. You bought 9 packets of potato chips from a store. Each packet costs 1.49 dollar and you gave shopkeeper 20 dollar. Find out using python, how many dollars is the shopkeeper going to give you back?
3. You want to replace tiles in your bathroom which is exactly square and 5.5 feet is its length. If tiles cost 500 rs per square feet, how much will be the total cost to replace all tiles. Calculate and print the cost using python (Hint: Use power operator ** to find area of a square)
4. Print binary representation of number 17
   
   [Solution](https://github.com/riteshsingh84/python/tree/main/Basics/02_numbers/exercise.py)
