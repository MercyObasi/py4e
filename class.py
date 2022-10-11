import math


class Phone:

    def design(self):
        ram = 4
        rom = 500
        print(ram, rom)


company = Phone()

company.design()

print(type(company))


class Computer:
    
    def __init__(self, cpu, ram):
        self.core = cpu
        self.pros = ram

    def config(self):
        print("config is:", self.core, self.pros)

    def update(self):
        self.pros = 8

    def compare(self, com2):
        if com1.core == com2.core:
            print("Same")
        else:
            print("Different")


com1 = Computer(ram=4, cpu="i3")
com2 = Computer(ram=10, cpu="i8")

com1.update()
com1.config()
com2.config()
com1.compare(com2)


# Types of Variables
class Car:

    tyres = 7  # Class/ Static variable

    def __init__(self):
        self.name = "Benz"  # Instance Variable
        self.mil = 12


c1 = Car()
c2 = Car()

Car.tyres = 4
c2.name = "BMW"

print(c1.name, c1.mil, Car.tyres)
print(c2.name, c2.mil, c2.tyres)


# Types of Method


class Student:

    school = "Emerald"

    def __init__(self,m1,m2,m3):
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3
        self.lap = self.Laptop  # Defining the inner class object inside the outer class object

    def avg(self):  # Instance Method
        return math.floor((self.m1 + self.m2 + self.m3)/3)

    def get_m2(self):  # Accessor Method
        return self.m2

    def set_m1(self, value):  # Mutators Method
        self.m1 = value

    @classmethod
    def school_name(cls):  # Class Method
        return cls.school

    @staticmethod
    def info():  # Static Method
        print("The total population of the school:", 345)

    class Laptop:

        def __init__(self):
            self.brand = "Lenovo"
            self.rom = "1TB"

        def show(self):
            print(self.brand, self.rom)


s1 = Student(23, 44, 95)

s2 = Student(30, 50, 78)
s2.set_m1(14)

print("Value for S2 set method:", s2.m1)

print("Value for S1 get method:", s1.get_m2())
print("The average of S1 is:", s1.avg())
print("The average of S2 is:", s2.avg())
print("The school name is:", Student.school_name())
Student.info()

lap1 = Student.Laptop()

lap1.show()


# Inheritance
class A:  # Parent/Super class
    def __init__(self):
        print("a init works")

    def feature1(self):
        print("feature1")

    def feature2(self):
        print("feature2")


class B(A):  # Child / Subclass

    def feature2(self):
        print("feature3")


b1 = B()


class C(B):  # Multi level class
    def __init__(self):
        print("c init works")
        super().__init__()


c1 = C()


class D(B, A):  # Multiple level class
    def __init__(self):
        print("d init works")
        super().__init__()  # Method Resolution Order, It calls A init as B doesn't have any

    def feature6(self):
        super().feature2()  # MRO - it goes from left-right, That's why it calls B feature instead of A feature


d1 = D()
d1.feature6()

