#   https://www.geeksforgeeks.org/python-convert-snake-case-to-pascal-case/?ref=leftbar-rightbar

def SnakePascal(test_str):
    res = test_str.replace("_"," ").title().replace(" ", "")
    return res

if __name__ == "__main__":
    test_str = 'geeksforgeeks_is_best'
    result = SnakePascal(test_str)
    print (result)