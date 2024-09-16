#   https://www.geeksforgeeks.org/python-program-to-generate-random-binary-string/?ref=leftbar-rightbar

import random

def RandomBinary(n): 
    num = random.getrandbits(n)
    bin_string = format(num, '0b')
    return bin_string

if __name__ == "__main__":
    n = 7 
    print("Random binary string of length {}: {}".format(n, RandomBinary(n)))