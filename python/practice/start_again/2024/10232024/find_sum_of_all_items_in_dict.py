#   https://www.geeksforgeeks.org/python-program-to-find-the-sum-of-all-items-in-a-dictionary/

def Sum(dict):
    list = []
    for i in dict:
        list.append(dict[i])
    return sum(list)

if __name__ == "__main__":
    dict = {'a': 100, 'b': 200, 'c': 300}
    print ("Sum of all items=", Sum(dict))