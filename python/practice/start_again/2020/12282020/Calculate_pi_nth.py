#Find PI to the Nth Digit - 
#Enter a number 
#and have the program generate PI up to that many decimal places. 
#Keep a limit to how far the program will go.
import math

def calculatepi(a):
    round_up = round(math.pi, a)
    print (round_up)

def main():
    a = int(input("Enter the Number to get your Nth place: "))
    max = 20
    if a <= max :
        calculatepi(a)
    else:
        print ("{} is greater than {}, Enter the less value ".format(a,max))

if __name__ == '__main__':
    main()