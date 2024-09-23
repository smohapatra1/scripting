#   https://www.geeksforgeeks.org/python-all-substrings-frequency-in-string/


def Sub(test_str):
    temp = [test_str[idx:j] for idx in range(len(test_str)) for j in range(idx +1 , len(test_str)+1)]
    d = dict()
    for i in temp:
        d[i] = test_str.count(i)
    return d


if __name__ == "__main__":
    test_str = 'abbca'
    result = Sub(test_str)
    print (result)