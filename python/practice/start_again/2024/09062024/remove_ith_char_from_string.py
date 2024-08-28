#   https://www.geeksforgeeks.org/ways-to-remove-ith-character-from-string-in-python/


def Remove(s):
    # Remove only 1st Occurrence
    new_str = s.replace('o', '', 1)
    # Remove all the occurrence
    new_str2 = s.replace('o', '')
    return new_str, new_str2


if __name__ == "__main__":
    s = "Sam is good"
    result = Remove(s)
    print (result)