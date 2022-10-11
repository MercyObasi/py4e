# Latitude and Longitude
from math import *
from numpy import *
avr = 6371.01
xx = float(input("Enter the latitude of point A: "))
zz = float(input("Enter the longitude of point A: "))
ww = float(input("Enter the latitude of point B: "))
yy = float(input("Enter the longitude of point B: "))
x = deg2rad(xx)
z = deg2rad(zz)
w = deg2rad(ww)
y = deg2rad(yy)
distance = avr * acos(sin(x)* sin(w)+ cos(x)* cos(w)* cos(z -y))
print(ceil(distance),"kilometers")