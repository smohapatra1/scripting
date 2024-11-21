#   https://www.geeksforgeeks.org/python-program-to-print-even-length-words-in-a-string/

def EvenLength(n):
    s = n.split(' ')
    p = []
    for  i in s :
        if len(i) % 2 == 0 :
            p.append(i)
    return p

if __name__ == "__main__":
    n = "This is a python language"
    print ("Current word          : ", n)
    print ("Even length words are : ", EvenLength(n))