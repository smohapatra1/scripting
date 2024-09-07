#   https://www.geeksforgeeks.org/python-consecutive-characters-frequency/

def ConsChar(test_str):
    res = [len(sub.group()) for sub in re.finditer(r'(.)\1*', test_str)]
    return res

if __name__ == "__main__":
    test_str = "geekksforgggeeks"
    result = ConsChar(test_str)
    print (result)