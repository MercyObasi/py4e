
def artist():
    print("Yemi Alade")
    h = len("Yemi Alade") >= 20
    print(h)

def songName():
    Music = "True Love"
    print(Music)
    y = len(Music) <= 8
    print(y)

def genre():
    Type = "Afrobeats"
    print(Type)
    x = len(Type) <= 10
    print(x)

artist()
songName()
genre()

"""
# Simple code using input
z = eval(input("Enter the equation: "))
print(z)
print(type(z))
"""

# Changing the code in command prompt
import sys
y = int(sys.argv[1])
d = int(sys.argv[2])
t = y + d
print(t)
