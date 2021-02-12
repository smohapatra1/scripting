#Print Fibonanci Series 
#

def main(n):
    fValue = 0 
    sValue = 1 
    for num in range(0, n):
        if num <=1:
            next = num
        else:
            next = fValue + sValue
            fValue = sValue
            sValue = next
        print (next, end=' ')

if __name__ == "__main__":
    n = int(input("Enter the number: "))
    main(n)