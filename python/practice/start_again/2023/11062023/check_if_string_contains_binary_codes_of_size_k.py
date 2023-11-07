# #   https://leetcode.com/problems/check-if-a-string-contains-all-binary-codes-of-size-k/

# 1461. Check If a String Contains All Binary Codes of Size K
# Medium
# 2.2K
# 92
# Companies
# Given a binary string s and an integer k, return true if every binary code of length k is a substring of s. Otherwise, return false.

 

# Example 1:

# Input: s = "00110110", k = 2
# Output: true
# Explanation: The binary codes of length 2 are "00", "01", "10" and "11". They can be all found as substrings at indices 0, 1, 3 and 2 respectively.
# Example 2:

# Input: s = "0110", k = 1
# Output: true
# Explanation: The binary codes of length 1 are "0" and "1", it is clear that both exist as a substring. 
# Example 3:

# Input: s = "0110", k = 2
# Output: false
# Explanation: The binary code "00" is of length 2 and does not exist in the array.


def binary_string( s: str , k=2) -> bool:
    codes = set()
    for i in range(len(s) -k +1):
        codes.add(s[i:i+k])
    return len(codes) == 2 ** k 




if __name__ == "__main__":
    s = "00110110"
    k = 2
    print ("{}".format(s, k))