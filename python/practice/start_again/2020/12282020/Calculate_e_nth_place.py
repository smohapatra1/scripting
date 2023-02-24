#Find e to the Nth Digit - 
#Just like the previous problem, but with e instead of PI. 
#Enter a number and have the program generate e up to that many decimal places. 
#Keep a limit to how far the program will go.
from math import e
import math
def calculatenumber(n):
    round_up = round(math.e,n)
    print (round_up)
def main():
    #Enter a number and the Nth place you want 
        a = input("Enter the number: ")
        n = int(input("Enter the numbers Nth place value "))
        if n <= 5:
            calculatenumber(n)
        else:
            print ("Enter a small value ")

if __name__ == '__main__':
    main()