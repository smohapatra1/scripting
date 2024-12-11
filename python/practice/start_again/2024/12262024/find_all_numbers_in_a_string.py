#   https://www.geeksforgeeks.org/find-all-the-numbers-in-a-string-using-regular-expression-in-python/

def GetNums(s):
    print (re.findall(r'[0-9]+', s))

if __name__ == "__main__":
    s = "adbv345hj43hvb42"
    GetNums(s)