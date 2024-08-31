#   https://www.geeksforgeeks.org/python-count-the-number-of-matching-characters-in-a-pair-of-string/


def countNum(string1, string2):
    return (len((set(string1)).intersection(set(string2))))

if __name__ == "__main__":
    # string1="SAMAR"
    # string2="SIA"
    string1 = 'aabcddekll12@'
    string2 = 'bb2211@55k'
    result = countNum(string1.lower(), string2.lower())
    print (result)