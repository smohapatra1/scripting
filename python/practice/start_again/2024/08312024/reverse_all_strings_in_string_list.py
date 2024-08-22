#   https://www.geeksforgeeks.org/python-reverse-all-strings-in-string-list/?ref=leftbar-rightbar

def Reverse(test_list):
    # res = [i[::-1] for i in test_list]
    res = [''.join(reversed(i)) for i in test_list]
    return res
if __name__ == "__main__":
    test_list = ["geeks", "for", "geeks", "is", "best"]
    result = Reverse(test_list)
    print (result)