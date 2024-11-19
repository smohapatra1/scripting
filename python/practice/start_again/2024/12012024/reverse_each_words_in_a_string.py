#   https://www.geeksforgeeks.org/problems/reverse-words-in-a-given-string5459/1

def Reverse(s):
    return ' '.join(x[::-1] for x in s.split(' '))

if __name__ == "__main__":
    s = " i like this program very much "
    print ("Before Reverse : ", s)
    print ("After Reverse  : ", Reverse(s))
