#   https://www.geeksforgeeks.org/python-permutation-given-string-using-inbuilt-function/

from itertools import permutations

def Permutation(string):
    s = permutations(string)
    for perm in s:
        print (''.join(perm))


if __name__ == "__main__":
    string = 'ABC'
    result = Permutation(string)