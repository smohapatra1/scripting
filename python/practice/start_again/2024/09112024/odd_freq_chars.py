#   https://www.geeksforgeeks.org/python-odd-frequency-characters/?ref=leftbar-rightbar

def Odd(test_str):
    s = set(test_str)
    res = []
    for i in s:
        if (test_str.count(i) % 2 != 0):
            res.append(i)
    return res 

if __name__ == "__main__":
    test_str = 'geekforgeeks is best for geeks'
    result = Odd(test_str)
    print (result)