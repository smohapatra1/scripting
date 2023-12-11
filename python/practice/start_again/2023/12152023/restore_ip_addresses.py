# #   https://leetcode.com/problems/restore-ip-addresses/

# 93. Restore IP Addresses
# Medium
# 5K
# 774
# Companies
# A valid IP address consists of exactly four integers separated by single dots. Each integer is between 0 and 255 (inclusive) and cannot have leading zeros.

# For example, "0.1.2.201" and "192.168.1.1" are valid IP addresses, but "0.011.255.245", "192.168.1.312" and "192.168@1.1" are invalid IP addresses.
# Given a string s containing only digits, return all possible valid IP addresses that can be formed by inserting dots into s. You are not allowed to reorder or remove any digits in s. You may return the valid IP addresses in any order.

 

# Example 1:

# Input: s = "25525511135"
# Output: ["255.255.11.135","255.255.111.35"]
# Example 2:

# Input: s = "0000"
# Output: ["0.0.0.0"]
# Example 3:

# Input: s = "101023"
# Output: ["1.0.10.23","1.0.102.3","10.1.0.23","10.10.2.3","101.0.2.3"]

from typing import List
def ip(s):
    return s == str(int (s) ) and int(s) <= 255

def restoreIpAddress(s: str)-> List[str]:
    n = len(s)
    ans = []
    for i in range(1, n ):
        for j in range(i+1, n ):
            for k in range(j+1, n ):
                a, b, c, d = s[:i], s[i:j], s[j:k], s[k:]
                if ip(a) and ip(b) and ip(c) and ip(d):
                    ans.append(f'{a}, {b}.{c}.{d}')
    return ans

if __name__ == "__main__":
    s = "25525511135"
    print ("{}".format(restoreIpAddress(s)))
