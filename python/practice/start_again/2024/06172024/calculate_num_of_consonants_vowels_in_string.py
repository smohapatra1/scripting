# Find the num of consonants and vowels in string 

def ConVow(s):
    numV = 0 
    numC = 0 
    d = s.lower()
    v = ('a', 'e', 'i', 'o', 'u' )
    for c in range(0, len(s)):
        if s[c] in v:
            numV = numV + 1
        elif s[c] >= 'a' and s[c] <= 'z':
            numC = numC + 1
    print ("Total Vowel are {} and Total Consonants {}".format(numV, numC))

if __name__ == "__main__":
    s = 'aaacdae'
    result = ConVow(s)

