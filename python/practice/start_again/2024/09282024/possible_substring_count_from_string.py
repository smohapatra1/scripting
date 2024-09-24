#   https://www.geeksforgeeks.org/python-possible-substring-count-from-string/

def Sstring(test_str, arg_str):
    res = min(test_str.count(i)// arg_str.count(i) for i in set(arg_str))
    return res

if __name__ == "__main__":
    test_str = "gekseforgeeks"
    arg_str = "geeks"
    result = Sstring( test_str, arg_str)
    print (result)