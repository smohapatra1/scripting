# #   https://leetcode.com/problems/length-of-last-word/
# 58. Length of Last Word
# Easy
# 4.2K
# 206
# Companies
# Given a string s consisting of words and spaces, return the length of the last word in the string.

# A word is a maximal 
# substring
#  consisting of non-space characters only.

 

# Example 1:

# Input: s = "Hello World"
# Output: 5
# Explanation: The last word is "World" with length 5.
# Example 2:

# Input: s = "   fly me   to   the moon  "
# Output: 4
# Explanation: The last word is "moon" with length 4.
# Example 3:

# Input: s = "luffy is still joyboy"
# Output: 6
# Explanation: The last word is "joyboy" with length 6.
 
# Approach
# Break the words, spaces etc 
# Keep the last word 
# Count that 

def last_word_length(s: str) -> int:
    # Solution-01
    #return len(s.split()[-1])
    # Solution -02
    a = s.split()
    if a :
        return len(a[-1])
    return 0


if __name__ == "__main__":
    #s= "hello world"
    s = "luffy is still joyboy"
    print ("{}".format(last_word_length(s)))