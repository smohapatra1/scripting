# 3. Longest Substring Without Repeating Characters

# Given a string s, find the length of the longest substring without repeating characters.

 

# Example 1:

# Input: s = "abcabcbb"
# Output: 3
# Explanation: The answer is "abc", with the length of 3.
# Example 2:

# Input: s = "bbbbb"
# Output: 1
# Explanation: The answer is "b", with the length of 1.
# Example 3:

# Input: s = "pwwkew"
# Output: 3
# Explanation: The answer is "wke", with the length of 3.
# Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.

def long_substring(word):
    # Using BFM 
    # If the entire string is unique, we can see that the required answer is the length of the string
    maxLength = 1 
    n=len(word)
    substring=''
    if word == '':
        return 0 
    # We can ravel through a loop and there will be two possibilities 
    # Given char in the string is either part of the longest substring or NOT
    for i in word:
        if i not in substring:
            substring = substring + i 
            maxLength = max(maxLength , len(substring))
            
        else:
            substring = substring.split(i)[1] + i 
    #print ("The substring is {}" .format(substring))
    #return maxLength
    print ("The substring is {} and it's length is {}" .format(substring,maxLength))

        

    # Using Set
    # n=len(word)
    # left=0
    # maxLength=0
    # charset=set()
    # word1=0
    # for right in range(n):
    #     if word[right] not in charset:
    #         charset.add(word[right])
    #         maxLength=max(maxLength, right - left +1)
    #     else:
    #         while word[right] in charset:
    #             charset.remove(word[left])
    #             left +=1
    #         charset.add(word[right])
    # return maxLength
if __name__ == "__main__":
    #word="pwwkew"
    word="abcabcbb"
    #word="bbbbb"
    long_substring(word)