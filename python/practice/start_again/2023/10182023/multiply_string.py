# #   https://leetcode.com/problems/multiply-strings/
# 43. Multiply Strings
# Medium
# 6.7K
# 3.1K
# Companies
# Given two non-negative integers num1 and num2 represented as strings, return the product of num1 and num2, also represented as a string.

# Note: You must not use any built-in BigInteger library or convert the inputs to integer directly.

 

# Example 1:

# Input: num1 = "2", num2 = "3"
# Output: "6"
# Example 2:

# Input: num1 = "123", num2 = "456"
# Output: "56088"


def multiply_string(num1: str , num2: str) -> str:
    if num1 == '0' or num2== '0':
        return '0'
    def decode (num):
        ans=0
        for i in num:
            ans=ans*10 + (ord(i) - ord('0'))
        return ans
    def encode (s):
        new =''
        while s:
            a = s%10
            s= s//10
            new=chr(ord('0')+ a) + new
        return new
    return encode(decode(num1)*decode(num2))



if __name__ == "__main__":
    num1 = "2"
    num2 = "3"
    print ("{}".format(multiply_string(num1, num2)))
