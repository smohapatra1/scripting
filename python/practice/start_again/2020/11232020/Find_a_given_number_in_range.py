#Write a function that checks whether a number is in a given range (inclusive of high and low)
def find_range(a,b,c):
    if a in range (b,c+1):
        print ("{} is in range {} and {}".format(a,b,c))
    else:
        print ("{} is not in range".format(a))
find_range(8,5,7)