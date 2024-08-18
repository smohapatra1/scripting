#   https://www.geeksforgeeks.org/python-program-to-check-if-the-list-contains-three-consecutive-common-numbers-in-python/
def CheckConsecutive(test_list):
    size = len(test_list)
    for i in range(size - 2):
        if test_list[i] == test_list[i+1 ] and test_list[i+1] == test_list[i+2]:
            print(test_list[i])

if __name__ == "__main__":
    test_list = [4, 5, 5, 5, 3, 8,11,11,11,12]
    result = CheckConsecutive(test_list)