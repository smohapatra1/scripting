#   https://www.geeksforgeeks.org/python-program-to-find-the-character-position-of-kth-word-from-a-list-of-strings/

def char_pos(test_list, K ):
    res = [ ele[0] for sub in enumerate(test_list) for ele in enumerate(sub[1]) ]
    return res[K]

if __name__ == "__main__":
    # test_list = ["geekforgeeks", "is", "best", "for", "geeks"]
    # K = 21
    test_list = ["geekforgeeks", "is", "best", "for", "geeks"]
    K = 15
    result = char_pos(test_list, K )
    print (result ) 
