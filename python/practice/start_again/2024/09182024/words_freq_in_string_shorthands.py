#   https://www.geeksforgeeks.org/python-words-frequency-in-string-shorthands/?ref=leftbar-rightbar

from collections import Counter

def Freq_in_String(test_str):
    # Solution - 01 
    # result = {key: test_str.count(key) for key in test_str.split()}
    # return result
    # Solution - 02 
    
    result=Counter(test_str.split())
    return dict(result)


if __name__ == "__main__":
    test_str = 'Gfg is best . Geeks are good and Geeks like Gfg'
    res = Freq_in_String(test_str)
    print (res) 