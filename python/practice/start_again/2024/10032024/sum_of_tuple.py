# https://www.geeksforgeeks.org/python-sum-of-tuple-elements/

def Sum(test_tup):
    count = 0 
    test = list(test_tup)
    for i in test:
        count = count + i 
    return count

if __name__ == "__main__":
    test_tup = (5, 20, 3, 7, 6, 8)
    result = Sum(test_tup)
    print (result)