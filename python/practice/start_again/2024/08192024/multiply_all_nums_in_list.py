#   https://www.geeksforgeeks.org/python-multiply-numbers-list-3-different-ways/

def MulList(list):
    num = 1
    for i in list:
        num = num * i 
    return num

if __name__ == "__main__":
    list = [ 10, 20, 1, 13, 12, 15]
    result = MulList(list)
    print (result)