# #   https://leetcode.com/problems/decode-string/
# 394. Decode String
# Medium
# 12K
# 551
# Companies
# Given an encoded string, return its decoded string.

# The encoding rule is: k[encoded_string], where the encoded_string inside the square brackets is being repeated exactly k times. Note that k is guaranteed to be a positive integer.

# You may assume that the input string is always valid; there are no extra white spaces, square brackets are well-formed, etc. Furthermore, you may assume that the original data does not contain any digits and that digits are only for those repeat numbers, k. For example, there will not be input like 3a or 2[4].

# The test cases are generated so that the length of the output will never exceed 105.

 

# Example 1:

# Input: s = "3[a]2[bc]"
# Output: "aaabcbc"
# Example 2:

# Input: s = "3[a2[c]]"
# Output: "accaccacc"
# Example 3:

# Input: s = "2[abc]3[cd]ef"
# Output: "abcabccdcdcdef"
 
def decode_string(s: str) -> str:
    stack=[]
    res=""
    num =0
    for i in s :
        if i.isdigit():
            num=num*10+int(i)
        elif i =="[":
            stack.append(res)
            stack.append(num)
            res=""
            num=0
        elif i == "]":
            prev_num=stack.pop()
            prev_str=stack.pop()
            res =   prev_str + prev_num* res
        else:
            res+=i
    return res 

if __name__ == "__main__":
    s = "3[a]2[bc]"
    print ("PRE {} and POST {}".format(s, decode_string(s)))