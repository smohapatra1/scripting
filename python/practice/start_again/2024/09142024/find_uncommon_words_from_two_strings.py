#   https://www.geeksforgeeks.org/python-program-to-find-uncommon-words-from-two-strings/


def uncommon(A, B ):
    a = A.split(' ')
    b = B.split(' ')
    x = []
    for i in a:
        if i not in b:
            x.append(i)
    for i in b:
        if i not in a:
            x.append(i)
    x = list(set(x))
    return x 

if __name__ == "__main__":
    A = "Geeks for Geeks"
    B = "Learning from Geeks for Geeks"
    result = uncommon(A, B )
    print (result)