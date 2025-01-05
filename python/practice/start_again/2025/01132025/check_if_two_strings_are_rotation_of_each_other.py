#   https://www.geeksforgeeks.org/a-program-to-check-if-strings-are-rotations-of-each-other/


def AreRotation(s1, s2):
    n = len(s1)
    for _ in range(n):
        if s1 == s2:
            return True
        s1 = s1[-1] + s1[:-1]
    return False

if __name__ == "__main__":
    s1 = "aab"
    s2 = "aba"
    s3 = "abcd"
    s4 = "abc"
    print ("True" if AreRotation(s1, s2) else "False")
    print ("True" if AreRotation(s3, s4) else "False")