#Find PI to the Nth Digit - 
#Enter a number 
#and have the program generate PI up to that many decimal places. 
#Keep a limit to how far the program will go.
#****************
# A test for me to print pi value to the places as you want 
from math import pi
import math
#print (round(pi,9))
#****************
def calculatepi(b):
    round_up = round(math.pi, b)
    pi = str(round_up)
    numlist=list(pi)
    print (round_up)
    return round_up
def main():
    # Make sure the number is decimal if not keep on asking..
    #while True:
        # Enter a number 
        #a = float(input('Enter a number : '))
    b = int(input("Enter the number of decimal places : "))
        #if a.is_integer():
        #    print ("Enter a decimal Number")
        #else:
        #    print ("You are Good with the number ", a)
    if b <= 40 :
        calculatepi(b)
    else:
        print ("Enter a lesser number")
        #    break

if __name__ == '__main__':
    main()