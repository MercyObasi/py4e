from functools import wraps # Prevents the function name from changings
from math import sqrt

# Decorators used for validations
def decorators(func):

    @wraps(func)
    def wrapper(*args, **kwargs):
        no = args[0]
        if not isinstance(no, int):
            raise ValueError
        square_root = func(*args, **kwargs)
        return f"This is the answer {square_root}"

    return wrapper

@decorators
def square_root(no):
    return sqrt(no)

print(square_root(25))
print(square_root.__name__)