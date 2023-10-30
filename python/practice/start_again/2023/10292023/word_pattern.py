# #   https://leetcode.com/problems/word-pattern/

# 290. Word Pattern
# Easy
# 6.8K
# 877
# Companies
# Given a pattern and a string s, find if s follows the same pattern.

# Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty word in s.

 

# Example 1:

# Input: pattern = "abba", s = "dog cat cat dog"
# Output: true
# Example 2:

# Input: pattern = "abba", s = "dog cat cat fish"
# Output: false
# Example 3:

# Input: pattern = "aaaa", s = "dog cat cat dog"
# Output: false


def num_patterns(pattern: str, s: str) -> bool:
    arr=s.split()
    if len(arr) != len(pattern):
        return False
    for i in range(len(arr)):
        if pattern.find(pattern[i]) != arr.index(arr[i]):
            return False
    return True




if __name__ == "__main__":
    pattern = "abba"
    #s = "dog cat cat dog"
    s = "dog cat cat cat dog"
    print ("{}".format(num_patterns(pattern, s )))