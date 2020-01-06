#Write a function that finds the magnitude of a given 3-dimensional vector. The magnitude of a vector is the square root of sum of squares of all the components of the vector.

#𝑚𝑎𝑔𝑛𝑖𝑡𝑢𝑑𝑒=𝑥2+𝑦2+𝑧2‾‾‾‾‾‾‾‾‾‾‾‾√)
import os
import math
def magnitude(x, y, z):
    m = (x ** 2 + y ** 2 + z ** 2) ** (1/2)
    print (m)
magnitude(2,3,-4)

