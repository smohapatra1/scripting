#   https://www.geeksforgeeks.org/python-dictionary-exercise/?ref=outind

def OrderSum(test_dict):
    temp = {keys: sum(map(lambda ele:ele, test_dict[keys])) for keys in test_dict}
    res = { keys: temp[keys] for keys in sorted(temp, key = temp.get)}
    return res

if __name__ == "__main__":
    test_dict = {'Gfg' : [6, 7, 4], 'is' : [4, 3, 2], 'best' : [7, 6, 5]} 
    print ("Results after ordering them : ", OrderSum(test_dict))