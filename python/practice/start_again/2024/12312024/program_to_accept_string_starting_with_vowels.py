#   https://www.geeksforgeeks.org/python-regex-program-to-accept-string-starting-with-vowel/

import re 

def StartVowel(a):
    regex = '^[aeiouAEIOU][A-Za-z0-9_]*'
    if re.search(regex, a):
        print ("It has vowels at the beginning ")
    else:
        print ("Doesn't have vowels in the beginning")

if __name__ == "__main__":
    a = "air"
    b = "beta"
    StartVowel(a)
    StartVowel(b)