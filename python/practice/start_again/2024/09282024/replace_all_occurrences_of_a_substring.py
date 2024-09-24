#   https://www.geeksforgeeks.org/python-replace-all-occurrences-of-a-substring-in-a-string/?ref=leftbar-rightbar

def Replace(input_string, s1, s2):
    res = input_string.replace(s1, s2)
    return res

if __name__ == "__main__":
    input_string = "geeksforgeeks"
    s1 = "geeks"
    s2 = "abcd"
    result = Replace(input_string, s1, s2)
    print (result)