def shout(text):
    return text.upper()

def whisper(text):
    return text.lower()

def greet(func):

    reply = func("Django is a nice framework")
    return reply

print(greet(shout))
print(greet(whisper))

# Returning a function
def create_adder(x):
    def adder(y):
        return x+y
 
    return adder
 
add_15 = create_adder(15)
 
print(add_15(10))
# decorators
import math
import time

def time_calculate(func):

    def inner1(*args, **kwargs):
        begin = time.time()
        func(*args, **kwargs)
        end = time.time()
        print(f"This is the time used from {begin} to {end} in {func.__name__}")
    return inner1

@time_calculate
def factorial_num(num):

    time.sleep(2)
    print(math.factorial(num))
    
factorial_num(10)

def another_decorator(func):
    def inner2(*args, **kwargs):
        print(f"before {func.__name__}")

        returned_value = func(*args, **kwargs)
        print(f"after {func.__name__}")

        return returned_value

    return inner2

@another_decorator
def add_num(a, b):
    print("inside add_num")
    return a + b

print("Sum=",add_num(2,4))

# code for testing decorator chaining
def decor1(func):
	def inner():
		x = func()
		return x * x
	return inner

def decor(func):
	def inner():
		x = func()
		return 2 * x
	return inner

@decor1
@decor
def num():
	return 10

print(num())

