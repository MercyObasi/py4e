# A python program to create user-defined exception
# class MyError is derived from super class Exception
from multiprocessing.sharedctypes import Value


class MyError(Exception):
 
    # Constructor or Initializer
    def __init__(self, value):
        self.value = value
 
    # __str__ is to print() the value
    def __str__(self):
        return(repr(self.value))
 
 
try:
    raise(MyError(3*2))
 
# Value of Exception is stored in error
except MyError as error:
    print('A New Exception occurred: ', error.value)

class Person:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def __repr__(self):
        return f"Name is {self.first_name} {self.last_name} and age is {self.age}"

person1 = Person("John","Rock", 24)
print(repr(person1))
print(str(person1))

class Area_error(Exception):
    max_area = 245
    min_area = 50
    def __init__(self, area, *args):
        super().__init__(args)
        self.area = area

    def __str__(self):
        return f"Area must be within {self.max_area} to {self.min_area}"

    def __name__(self):
        return self.__name__


def area_rectangle(b, a):
    area = b * a
    if area > Area_error.max_area or area < Area_error.min_area:
        raise Area_error(area)

    return area

if __name__ == '__main__':
    b = input("Please enter your length: ")
    a = input("Please enter your breadth: ")
    try:
        b = float(b)
        a = float(a)
    except ValueError as ex:
        print(ex,"\nPlease enter a valid input")
    else:
        try:
            result = area_rectangle(b, a)
        except Area_error as e: 
            print(e)
        else:
            print(f"Action successful\n Your area is {result}")
        