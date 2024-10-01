#   https://www.geeksforgeeks.org/python-sort-tuples-by-total-digits/

def TotalDigits(test_list):
    return sum([len(str(ele)) for ele in test_list])

test_list.sort(key = TotalDigits)
print("Sorted tuples : " + str(test_list))

if __name__ == "__main__":
    test_list = [(3, 4, 6, 723), (1, 2), (12345,), (134, 234, 34)]
    result = TotalDigits(test_list)