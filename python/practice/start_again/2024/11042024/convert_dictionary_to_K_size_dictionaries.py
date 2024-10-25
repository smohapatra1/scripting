#   https://www.geeksforgeeks.org/python-convert-dictionary-to-k-sized-dictionaries/

def KSized(test_dict, K ):
    res = [dict(list(test_dict.items()) [i:i+K]) for i in range(0, len(test_dict), K )]
    return res

if __name__ == "__main__":
    test_dict = {'Gfg' : 1, 'is' : 2, 'best' : 3, 'for' : 4, 'geeks' : 5, 'CS' : 6}
    K = 2 
    print ("Results after converting : ", KSized(test_dict, K ))