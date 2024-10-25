#   https://www.geeksforgeeks.org/ways-to-convert-string-to-dictionary/?ref=leftbar-rightbar

def StrDict(str):
    res = dict(val.split("=") for val in str.split(";"))
    return res

if __name__ == "__main__":
    str = " Jan = January; Feb = February; Mar = March"
    print ("Results after converting Str to Dict : ", StrDict(str)) 