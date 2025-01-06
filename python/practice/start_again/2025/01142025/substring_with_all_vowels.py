#   https://www.geeksforgeeks.org/find-substrings-contain-vowels/

def isVowels(x):
    if (x == 'a' or x == 'e' or x == 'i' or x == 'o' or x == 'u'):
        return True
    return False

def SubstringWithVowels(s):
    n = len(s)
    for i in range(n):
        hash = dict()
        for j in range(i, n ):
            if (isVowels(s[j]) == False):
                break 
            hash[s[j]] = 1
            if len(hash) == 5:
                print (s[i:j +1 ], end = ' ')

if __name__ == "__main__":
    s = 'aeoibddaeoiud'
    SubstringWithVowels(s)