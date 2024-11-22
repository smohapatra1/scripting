#   https://www.geeksforgeeks.org/python-sum-of-tuple-elements/

def summation(test_tup):
    count = 0 
    for i in test_tup:
        count = count + i 
    return count


if __name__ == "__main__":
    test_tup = (5, 20, 3, 7, 6, 8)
    print(summation(test_tup))