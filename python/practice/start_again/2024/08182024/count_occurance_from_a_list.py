#   https://www.geeksforgeeks.org/python-count-occurrences-element-list/

def CountOccur(list, x):
    # count = 0 
    # for i in list:
    #     if i == x:
    #         count = count +1
    # return count
    # Solution - 2 - List Comprehension 
    y = [i for i in list if i == x]
    return len(y)

if __name__ == "__main__":
    list = [ 1, 2, 4, 5, 1, 5 ]
    x = 5 
    result = CountOccur(list, 5 )
    print (result)