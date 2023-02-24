# Find the factors of a number 
def main():
    n = int(input("Enter a number "))
    i = 1
    a = []
    while i <=n:
        if n % i == 0 :
            #print ("The Factors are %d for num %d" % (i, n)) 
            a.append(i)
        i +=1
    print ("The factors are %s for num %d " %(a, n))
        
if __name__ == "__main__":
    main()