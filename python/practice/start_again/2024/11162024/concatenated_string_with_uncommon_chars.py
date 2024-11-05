#   https://www.geeksforgeeks.org/concatenated-string-uncommon-characters-python/

def unconcatenated(str1, str2):
    s1 = set(str1)
    s2 = set(str2)
    common = list(s1 ^ s2)
    print (''.join(common))

if __name__ == "__main__":
    str1 = 'aacdb'
    str2 = 'gafd'
    unconcatenated(str1, str2)