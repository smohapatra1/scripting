#   https://www.geeksforgeeks.org/problems/mark-even-and-odd/1

def CheckOddEven(s):
    if s > 0:
        if s % n == 0 and s % 2 == 0 :
            return 'Even'
        else:
            return 'Odd'

if __name__ == "__main__":
    s = 24
    print ("The entered number ", s , "is :  ", CheckOddEven(s))