# https://www.geeksforgeeks.org/python-program-to-print-all-odd-numbers-in-a-range/

def Print_Odd(a, b ):
    for i in range(a, b+1):
        if i % 2 != 0:
            print (i, end=' ')


if __name__ == "__main__":
    a = int(input("Enter a start number : "))
    b = int(input("Enter a end number "))
    result = Print_Odd(a, b )
