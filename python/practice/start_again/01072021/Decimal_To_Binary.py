#Convert Decimal to Binary 
#Deide with integral result and discard reminder 

def DecimalToBinary(d):
    if d > 1 :
        DecimalToBinary(d//2)
    print (d%2 , end=' ')
def main():
    d = int(input("Enter the decimal number: "))
    DecimalToBinary(d)

if __name__ == "__main__":
    main()