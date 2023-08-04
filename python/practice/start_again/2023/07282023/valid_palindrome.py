# 125. Valid Palindrome
# A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. 
# Alphanumeric characters include letters and numbers.

# Given a string s, return true if it is a palindrome, or false otherwise.
# Example 1:

# Input: s = "A man, a plan, a canal: Panama"
# Output: true
# Explanation: "amanaplanacanalpanama" is a palindrome.

# Example 2:

# Input: s = "race a car"
# Output: false
# Explanation: "raceacar" is not a palindrome.

#   Solution 
#   Remove the spaces and punctuation 
#   Convert them into lowercase using link comprehension 
#   Join them into a new string 
#   Find the string with Start and End indices 
#   Now look for first and last letters of the string, if they matches it's good, Go to next letter
#   Keep doing that check until it runs out of letters to check 
#   If it doesn't find a pair, return false
#   The process continues until either the indices cross each other or a mismatch found 


#   OR
#   Using built in functions 


def palindrome( word: str) -> bool:
    # word1=""
    # for i in word:
    #     if i.isalpha():word1 +=i.lower()
    #     if i.isnumeric():word1 +=i
    # return word1 == word1[::-1]
    word=[char.lower() for char in word if word.isalnum()]
    return word == word[::-1]
    

if __name__ == "__main__":
    word="A man, a plan, a canal: Panama"
    print ("The word is : {}".format(word))
    print ("The '{}' is Palindrome: {}".format(word, palindrome(word)))


