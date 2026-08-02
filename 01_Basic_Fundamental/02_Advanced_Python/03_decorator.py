'''
Problem Statement 1 — Build Your Own Logger Decorator
Requirements

Create a decorator that:

Accepts any function.
Prints:
Starting <function_name>

before execution.

Prints:
Finished <function_name>

after execution.

Returns the original result.
Constraints
Do not use functools.wraps in the first version.
Support any arguments using *args and **kwargs.
Return the original function's return value.
'''



def logger(function):
    def wrapper(*args,**kwargs):
        print(f"Starting {function.__name__}")

        result = function(*args,**kwargs)

        print(f"Finished {function.__name__}")

        return result

    return wrapper



@logger
def add(a,b):
    return a+b

answer = add(10,20)

print(answer)