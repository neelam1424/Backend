'''
Requirements

Create a decorator that:

Measures execution time.
Prints the elapsed time.
Returns the original result.

Use:

time.perf_counter()
'''

import time

def timer(function):
    def wrapper(*args,**kwargs):
        start_time = time.perf_counter()

        result = function(*args, **kwargs)

        end_time = time.perf_counter()

        elapsed_time = end_time - start_time


        print(
            f"{function.__name__} took"
            f"{elapsed_time:.6f} seconds"
        )

        return result
    return wrapper


@timer
def slow_add(a, b):
    time.sleep(2)
    return a + b


answer = slow_add(10, 20)

print("Result:", answer)