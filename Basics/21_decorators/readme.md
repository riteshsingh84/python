# Python Decorators

In Python, decorators are a powerful and expressive tool that allow you to modify or enhance the behavior of functions or classes without changing their actual code. They are often used for logging, access control, memoization, and more.

## 🧩 Basic Concept 
A decorator is a function that takes another function (or method) as an argument, adds some kind of functionality to it, and returns a new function.

## Example
    def my_decorator(func):
        def wrapper():
            print("Something is happening before the function is called.")
            func()
            print("Something is happening after the function is called.")
        return wrapper

    @my_decorator
    def say_hello():
        print("Hello!")

    say_hello()

### Output:
    Something is happening before the function is called.
    Hello!
    Something is happening after the function is called.

## 🧰 Common Use Cases
* Logging
* Authentication/Authorization
* Caching (Memoization)
* Timing function execution
* Input validation


## 🧠 Exercise
1. Create a decorator function to check that the argument passed to the function factorial is a non-negative integer:

2. Create a factorial function which finds the factorial of a number.

3. Use the decorator to decorate the factorial function to only allow factorial of non-negative integers.

Example: 

    factorial(1.354) : raise Exception or print error message
    factorial(-1) : raise Exception or print error message
    factorial(5) : 60


   
   [Solution](https://github.com/riteshsingh84/python/tree/main/Basics/21_decorators/exercise.py)
