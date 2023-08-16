# 76. Minimum Window Substring

# Given two strings s and t of lengths m and n respectively, 
# return the minimum window substring
# of s such that every character in t (including duplicates) is included in the window. 
# If there is no such substring, return the empty string "".

# The testcases will be generated such that the answer is unique.

 

# Example 1:

# Input: s = "ADOBECODEBANC", t = "ABC"
# Output: "BANC"
# Explanation: The minimum window substring "BANC" includes 'A', 'B', and 'C' from string t.


# Example 2:

# Input: s = "a", t = "a"
# Output: "a"
# Explanation: The entire string s is the minimum window.
# Example 3:

# Input: s = "a", t = "aa"
# Output: ""
# Explanation: Both 'a's from t must be included in the window.
# Since the largest window of s only has one 'a', return empty string.

from collections import Counter

def minWindow(s,t):
    req = Counter(t) # Hash table to store the char frequency 
    missing=len(t)   # Total number of chars we care 
    i = 0
    start = 0 
    end = 0
    for j, char in enumerate(s, 1): # Index j from 1 
        missing -= req[char] > 0 
        req[char] -=1
        if not missing:
            while req[s[i]] < 0: 
                req[s[i]] +=1
                i+=1
            if not end or j - i <= end - start: # Update Window
                start, end = i, j 
                req[s[i]] += 1  
                i +=1       # Update i to start+1 for next window 
                missing +=1 # We missed the first chars, so add missing by 1 
    return s[start:end] 




if __name__ == "__main__":
    s = "ADOBECODEBANC"
    #s ="ABCDOODEBANC"
    t = "ABC"
    print ("The characters are {}".format(minWindow(s,t)))

