#Sprint the numbers 

def main():
    n = int(input("Enter a number: "))
    count = 0
    temp = n
    while temp > 0 :
        temp = temp//10
        count = count + 1
    print ("The number of digits are %d in %d " % (count, n))
    
if __name__ == "__main__":
    main()