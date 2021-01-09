#Binary to Decimal and Back Converter -
# Develop a converter to convert a decimal number to binary 
#or a binary number to its decimal equivalent.
import math

def DecimalToBinary(a):
    #if a > 1 :
    #    DecimalToBinary(a//2)
    #print (a%2, end=' ')
    # Other way 
    print ("Decimal (%d) to Binary (%d) "  %(a, int(bin(a)[2:])))

def BinaryToDecimal(b):
    ar = [int(i) for i in b ]
    ar = ar[::-1]
    result = []
    for i in range(len(ar)):
        result.append(ar[i]*(2**i))
    res_sum = sum(result)
    print ("Binary (%s) to Decimal (%d) " %(b, res_sum))

def main():
    a = int(input("Enter a decimal number :" ))
    b = input("Enter a binary number : ")
    DecimalToBinary(a) # https://www.geeksforgeeks.org/binary-decimal-vice-versa-python/
    BinaryToDecimal(b)
if __name__ == "__main__":
    main()
    