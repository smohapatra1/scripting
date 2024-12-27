#!/usr/bin/python
#Write a Python program which accepts the radius of a circle from the user and compute the area.
from math import pi
r = int(input("Enter the radius : "))
area = float(pi * r ** 2)
print ("Area %s " %area )
