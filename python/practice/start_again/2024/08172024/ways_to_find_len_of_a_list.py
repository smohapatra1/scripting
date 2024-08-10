#   https://www.geeksforgeeks.org/python-ways-to-find-length-of-list/

def LenList(List):
    # Ways - 1 
    # print ("Length of the list is using Len : ", len(List))
    # Ways - 2 
    # Counter = 0 
    # for i in List:
    #     Counter = Counter +1 
    # return Counter
    # Ways - 3 
    len = sum(1 for i in List)
    return len

if __name__ == "__main__":
    List = [10, 11, 15, 18, 20]
    result = LenList(List)
    print (result)