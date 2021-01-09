# Write script to convert decimal to Binary and vice versa

def convert(b,d):
    #Decimal to Binary 
    print ("Decimal to Binary - ", bin(d)[2:])
    #Binary to Decimal
    ar = [int(i) for i in b]
    ar = ar[::-1]
    result = []
    for i in range(len(ar)):
        result.append(ar[i]*(2**i))
        Total = sum(result)
    print ("Binary to Decimal - ", Total) 

def main():
    b = input("Enter a Binary Number : ")
    d = int(input("Enter a Decimal Number : "))
    convert(b,d)

if __name__ == "__main__":
    main()