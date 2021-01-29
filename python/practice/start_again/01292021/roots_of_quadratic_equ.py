#Python Program to find roots of a Quadratic Equation
#Write a Python program to find Roots of a Quadratic Equation with an example. 
# The mathematical representation of a Quadratic Equation is ax²+bx+c = 0. 
# A Quadratic Equation can have two roots, and they depend entirely upon the discriminant. 
# If discriminant > 0, then Two Distinct Real Roots exists for this equation
#https://www.tutorialgateway.org/python-program-to-find-roots-of-a-quadratic-equation/

import math

def main():
    a = int(input("Enter the valud of a : "))
    b = int(input("Enter the value of b: "))
    c = int(input("Enter the value of c: "))
    discriminant = (b * b ) - ( 4 * a * c)
    if discriminant > 0 :
        root1 = (-b + math.sqrt(discriminant))/2 * a 
        root2 = (-b - math.sqrt(discriminant))/2 * a 
        print ("Two distinct Real Roots exist : root1 = %.2f and root2 = %.2f" % (root1, root2))
    elif (discriminant < 0):
        root1 = root2 = -b /(2*a)
        imaginary = math.sqrt (-discriminant )/2 * a 
        print ("Two distinct Complex roots exists: root1 = %.2f + %.2f and root2 = %.2f - %.2f " %(root1, imaginary, root2, imaginary))
    elif ( discriminant == 0 ):
        root1 = root2 = -b / (2*a)
        print ( "Tow Equal and real roots exists : root1 = %.2f and root2 = %.2f " % (root1, root2))

if __name__ == "__main__":
    main()