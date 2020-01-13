#Write a function that finds the distance between two points and returns it. The distance between two points with x,y, and z components can be calculated as:
#𝑑𝑖𝑠𝑡𝑎𝑛𝑐𝑒=(𝑥2−𝑥1)2+(𝑦2−𝑦1)2+(𝑧2−𝑧1)2‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾√ 
from math import * 
def dist1( x1, y1, z1, x2, y2, z2 ):
    distance = sqrt ( ( x2 -x1)**2 + ( y2 - y1 )**2 + (z2 -z1)**2 )
    print (distance)
dist1(2, 3 , -5, 4, -3, 12)
