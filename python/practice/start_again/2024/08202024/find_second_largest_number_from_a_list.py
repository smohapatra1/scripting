#   https://www.geeksforgeeks.org/python-program-to-find-second-largest-number-in-a-list/


def SecondLargest(list):
    list.sort()
    return list[-2]

if __name__ == "__main__":
    list = [ 10, 1, 2, 6, 19, 20 , 22, 100]
    result = SecondLargest(list)
    print (result)