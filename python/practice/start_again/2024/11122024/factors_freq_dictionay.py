#   https://www.geeksforgeeks.org/python-factors-frequency-dictionary/

def factors(test_list):
    res = dict()
    for idx in range(1, max(test_list)):
        res[idx] = sum(key % idx == 0 for key in test_list)
    return res

if __name__ == "__main__":
    test_list = [2, 4, 6, 8, 3, 9, 12, 15, 16, 18]
    print("Results after finding the factors: ", factors(test_list))