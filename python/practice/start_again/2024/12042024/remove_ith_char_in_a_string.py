#   https://www.geeksforgeeks.org/ways-to-remove-ith-character-from-string-in-python/

def RemoveChar(s):
    return s.replace("king", "king of king")

if __name__ == "__main__":
    s = 'I am the king'
    print ("Current String: ", s )
    print ("String after removing a char ", RemoveChar(s))