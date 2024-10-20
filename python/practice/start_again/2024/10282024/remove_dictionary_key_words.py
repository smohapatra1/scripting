#   https://www.geeksforgeeks.org/python-remove-dictionary-key-words/?ref=leftbar-rightbar

def Replace(test_str, test_dict):
    temp = test_str.split(' ')
    temp1 = [ word for word in temp if word.lower() not in test_dict]
    res = ' '.join(temp1)
    return res
if __name__ == "__main__":
    test_str = 'gfg is best for geeks'
    test_dict = {'geeks': 1, 'best': 6}
    print ("The string after replace : ", Replace(test_str, test_dict))