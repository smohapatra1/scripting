#   #   https://www.geeksforgeeks.org/problems/reverse-words-in-a-given-string5459/1

def Reverse(s):
    s = s.split()[::-1]
    l = []
    for i in s :
        l.append(i)
    return ' '.join(l)

if __name__ == "__main__":
    s = " i like this program very much "
    print ("Current Word  : ", s)
    print ("After reverse : ", Reverse(s))