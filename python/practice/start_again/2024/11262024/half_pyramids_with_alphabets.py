#   https://www.geeksforgeeks.org/programs-printing-pyramid-patterns-python/#example-2-full-pyramid-patterns-in-python-recursion

def Alphabets(n):
    # ASCII char
    num = 65
    for i in range(0, n ):
        for j in range(0, i+1):
            ch = chr(num)
            print (ch, end=" ")
        num = num+1
        print ("\r")
        
if __name__ == "__main__":
    n = 5 
    Alphabets(n)