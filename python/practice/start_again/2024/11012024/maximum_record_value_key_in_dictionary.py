#   https://www.geeksforgeeks.org/python-maximum-record-value-key-in-dictionary/?ref=leftbar-rightbar

def HighestKey(test_dict):
    key = 'Himani'
    res = max(test_dict, key=lambda sub: test_dict[sub][key])
    return res
if __name__ == "__main__":
    test_dict = {'gfg' : {'Manjeet' : 5, 'Himani' : 10},
             'is' : {'Manjeet' : 8, 'Himani' : 9},
             'best' : {'Manjeet' : 10, 'Himani' : 15}}
    print ("Keys with highest values are: ", HighestKey(test_dict))