#Write a function that computes the volume of a sphere given its radius.
#Volume = 4/3 * pi * r**2
from math import pi
def volume(x):
    v = ( (4/3) * pi * (x**3))
    print ("The volume is {}".format(v))
volume(input("Enter the the radius : "))