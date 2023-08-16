# 567. Permutation in String

# Given two strings s1 and s2, return true if s2 contains a permutation of s1, or false otherwise.

# In other words, return true if one of s1's permutations is the substring of s2.

 

# Example 1:

# Input: s1 = "ab", s2 = "eidbaooo"
# Output: true
# Explanation: s2 contains one permutation of s1 ("ba").
# Example 2:

# Input: s1 = "ab", s2 = "eidboaoo"
# Output: false


from collections import Counter

def permutation(s1, s2 ):
    # Solution - 01 

    n1=len(s1)
    n2=len(s2)
    center=Counter(s1)
    matched=0
    for i in range (n2):
        if s2[i] in center:
            center[s2[i]] -=1
            if center[s2[i]] == 0:
                matched +=1
        if i >= n1 and s2[i-n1] in center:
            if center[s2[i-n1]] ==0:
                matched -= 1
            center[s2[i-n1]] +=1
        if matched == len(center):
            return True
    return False

    #Solution 02
    # n1=len(s1)
    # n2=len(s2)
    # counter=Counter(s1)
    # for i in range(n2):
    #     if s2[i] in counter:
    #         counter[s2[i]] -=1
    #     if i >= n1 and s2[i-n1] in counter:
    #         counter[s2[i-n1]] +=1
    #     if all([counter[i] ==0 for i in counter ]):
    #         return True
    # return False 

if __name__ == "__main__":
    s1="ab"
    s2 = "eidbaooo"
    #s2 = "eidboaoo"
    print("{} and {} Permutation :- {}".format(s1, s2, permutation(s1, s2 )))