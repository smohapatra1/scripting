#Find the first digit of a number 
def main():
    n = int(input("Enter your number : "))
    count = 0 
    temp = n 
    while temp >= 10 :
        temp = temp // 10
        count +=1
    print ("The first digit is %d in Number %d" %(temp,n))
if __name__ == "__main__":
    main()