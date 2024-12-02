#   https://www.geeksforgeeks.org/python-program-to-find-volume-surface-area-and-space-diagonal-of-a-cuboid/

from math import sqrt

def SurfaceArea(l, b , h ):
    return (2* (l*b + b*h + h*l))
def Volume(l, b, h):
    return l*b*h
def SpaceDiagonal(l, b , h ):
    return (sqrt(l**2 + b**2 + h**2))

if __name__ == "__main__":
    l = 9 
    b = 6 
    h = 10 
    print ("Surface Area : ",SurfaceArea(l, b , h ))
    print ("Volume       : ",Volume(l, b , h ))
    print ("Space Diagnl : ",SpaceDiagonal(l, b , h ))
