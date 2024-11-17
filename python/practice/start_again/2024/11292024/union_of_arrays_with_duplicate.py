#   https://www.geeksforgeeks.org/problems/union-of-two-arrays3538/1
import itertools

def Union(a, b ):
    print (a +b) # With duplicates
    print (list(set(a+b))) # Without duplicates
    print (list(itertools.chain(a, b ))) # With duplicates

if __name__ == "__main__":
    a = [ 1, 5, 6, 9, 2, 3]
    b = [ 5, 1, 10, 12, 14, 3]
    Union(a, b )