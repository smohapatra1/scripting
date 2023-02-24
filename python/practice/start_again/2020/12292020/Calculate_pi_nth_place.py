#Calculate pi's Nth Place 
import math
from math import pi

def Calculate(a):
    a=round(math.pi,a)
    print (a)
def main():
    a = int(input("Enter the number's Nth place you want: "))
    max = 10 
    if a <=max:
        Calculate(a)
    else:
        print ("Please enter lesser values ")

if __name__ == '__main__':
    main()