#LESSER OF TWO EVENS: Write a function that returns the lesser of two given numbers if both numbers are even, 
#but returns the greater if one or both numbers are odd
#lesser_of_two_evens(2,4) --> 2
#lesser_of_two_evens(2,5) --> 5
def even(a,b):
    if a % 2 == 0 and b % 2 == 0 :
        if a < b :
            print (a)
    if a % 2 != 0 and b % 2 != 0 :
        if a < b :
            print (b)
even(5,7)

#You can use min and max functions 

def even1(a,b):
    if a % 2 == 0 and b % 2 == 0 :
        return min(a,b)
    else:
        return max(a,b)
even(5,11)