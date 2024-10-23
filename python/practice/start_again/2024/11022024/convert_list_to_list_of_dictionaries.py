#   https://www.geeksforgeeks.org/python-convert-list-to-list-of-dictionaries/?ref=leftbar-rightbar

def ListDict(test_list):
    key_list = ["name", "number"]
    n = len(test_list)
    res = []
    for idx in range(0, n , 2):
        res.append({key_list[0]: test_list[idx], key_list[1] : test_list[idx+1]})
    return res 
if __name__ == "__main__":
    test_list = ["Gfg", 3, "is", 8, "Best", 10, "for", 18, "Geeks", 33]
    print ("Results after converting list to Dict: ", ListDict(test_list))
