#   https://www.geeksforgeeks.org/python-program-to-print-all-positive-numbers-in-a-range/

def PositiveNum(start, end):
    for i in range(start, end+1):
        if i > 0:
            print (i, end=' ')
if __name__ == "__main__":
    start = int(input("Enter the start number: "))
    end = int(input("Enter the end number: "))
    result = PositiveNum(start, end)