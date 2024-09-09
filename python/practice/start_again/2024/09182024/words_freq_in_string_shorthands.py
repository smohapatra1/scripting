#   https://www.geeksforgeeks.org/python-words-frequency-in-string-shorthands/?ref=leftbar-rightbar


def Freq_in_String(test_str):
    result = {key: test_str.count(key) for key in test_str.split()}
    return result

if __name__ == "__main__":
    test_str = 'Gfg is best . Geeks are good and Geeks like Gfg'
    res = Freq_in_String(test_str)
    print (res) 