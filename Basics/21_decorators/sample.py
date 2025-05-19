import time

# The time_it decorator is used to measure the execution time of the functions calc_square and calc_cube.
# It wraps the original function, records the start time before calling it, and calculates the elapsed time after the function call.
def time_it(func):
    """
    Decorator to measure the execution time of a function.
    """
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"{func.__name__} execution time: {(end_time - start_time)*1000:.4f} ms")
        return result
    return wrapper


# The calc_square and calc_cube functions are decorated with the time_it decorator.
@time_it
def calc_square(numbers):
   result = []
   for number in numbers:
       result.append(number * number)
   return result

@time_it
def calc_cube(numbers):
   result = []
   for number in numbers:
       result.append(number * number * number)       
   return result

# The range function generates a sequence of numbers from 1 to 99999.
# The calc_square and calc_cube functions are called with this sequence, and their execution times are measured.
array_of_numbers = range(1, 100000)
calc_square(array_of_numbers)
calc_cube(array_of_numbers)
