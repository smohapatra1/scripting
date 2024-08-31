#   https://www.geeksforgeeks.org/python-program-to-accept-the-strings-which-contains-all-vowels/


def check(string):
    if len(set(string.lower()).intersection("aeiou")) >=5 :
        return ("accepted")
    else:
        return ('not accepted')

if __name__ == "__main__":
    # string = "SEEquoiaL"
    string = "geeksforgeeks"
    result = check(string)
    print (result)