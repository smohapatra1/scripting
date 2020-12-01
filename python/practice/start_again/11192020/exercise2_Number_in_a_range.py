#Write a function that checks whether a number is in a given range (inclusive of high and low)
def greater(num1,low,high):
    if num1 in range (low,high+1):
        print ("{} is in range {} and {}".format(num1,low,high))
    else:
        print ('Not in Range ')
greater(5,2,7)
