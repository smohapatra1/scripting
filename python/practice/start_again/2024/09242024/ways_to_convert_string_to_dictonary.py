#   https://www.geeksforgeeks.org/ways-to-convert-string-to-dictionary/?ref=leftbar-rightbar

def StrDict(str):
    res = dict(subString.split('=') for subString in str.split(';'))
    return res

if __name__ == "__main__":
    str = " Jan = January; Feb = February; Mar = March"
    result = StrDict(str)
    print (result)