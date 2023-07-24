# Define decorator that calculate the time to run a function

from functools import wraps
import time


def time_calculator(function):
    @wraps(function)
    def wrapper(*args, **kwargs):
        t1 = time.time_ns()
        returned_value = function(*args, **kwargs)
        t2 = time.time_ns()
        print(t2-t1)
        return returned_value
    return wrapper


@time_calculator
def add(a, b):
    return a+b


print(add(3, 14))

