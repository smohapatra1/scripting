#   https://www.geeksforgeeks.org/python-set-check-string-panagram/

from string import ascii_lowercase as asc_lower

def Pangram(s):
    return set(asc_lower) - set(s.lower()) == set([])
    if Pangram(s) == True:
        print ("The String is Pangram")
    else:
        print ("The String is NOT Pangram")


if __name__ == "__main__":
    # s = "The quick brown fox jumps over the lazy dog"
    s = "geeks for geeks"
    print ("The string is Pangram : ", Pangram(s))