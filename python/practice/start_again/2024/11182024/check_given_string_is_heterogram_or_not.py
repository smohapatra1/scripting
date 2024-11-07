#   https://www.geeksforgeeks.org/python-set-check-whether-given-string-heterogram-not/

def heterogram(input):
    alphabets = [ ch for ch in input if (ord(ch) >= ord('a') and ord(ch) <= ord('z'))]
    if len(set(alphabets)) == len(alphabets):
        print ('Yes')
    else:
        print ('No')

if __name__ == "__main__":
    input = 'the big dwarf only jumps '
    heterogram(input)