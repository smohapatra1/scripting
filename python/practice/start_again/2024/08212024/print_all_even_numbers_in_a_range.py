#   https://www.geeksforgeeks.org/python-program-to-print-all-even-numbers-in-a-range/

def Print_Even(a, b ):
    for i in range(a, b+1):
        if i % 2 == 0:
            print (i, end=' ')


if __name__ == "__main__":
    a = int(input("Enter a start number : "))
    b = int(input("Enter a end number "))
    result = Print_Even(a, b )
