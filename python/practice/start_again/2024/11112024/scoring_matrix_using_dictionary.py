#   https://www.geeksforgeeks.org/python-scoring-matrix-using-dictionary/

def Scoring(test_list, test_dict):
    res = [sum(test_dict[word] if word.lower() in test_dict else 0 for word in sub ) for sub in test_list]
    return res
if __name__ == "__main__":
    test_list = [['gfg', 'is', 'best'], ['gfg', 'is', 'for', 'geeks']]
    test_dict = {'gfg' : 5, 'is' : 10, 'best' : 13, 'for' : 2, 'geeks' : 15}
    print ("Results after scoring: ", Scoring(test_list, test_dict))