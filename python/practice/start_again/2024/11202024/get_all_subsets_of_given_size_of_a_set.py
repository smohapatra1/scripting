#   https://www.geeksforgeeks.org/python-program-to-get-all-subsets-of-given-size-of-a-set/
import itertools

def Subset(s, n ):
    return list(itertools.combinations(s,n))


if __name__ == "__main__":
    s = {1, 2, 3}
    n = 2
    print ("Subsets are : ", Subset(s, n ))