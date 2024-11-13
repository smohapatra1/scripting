#   https://www.geeksforgeeks.org/python-program-to-print-the-natural-numbers-summation-pattern/

def Natural(n):
    for i in range(1, n+1):
        a = []
        for j in range(1, i+1):
            print (j, sep=" ", end=" ")
            if i < j :
                print ("+",sep=" ", end=" ")
            a.append(i)
        print ("=",sum(a))
    print ()

if __name__ == "__main__":
    n = 5 
    Natural(n)