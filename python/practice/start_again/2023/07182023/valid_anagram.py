# #Given two strings s and t, return true if t is an anagram of s, and false otherwise.

# An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

# Example 1:

# Input: s = "anagram", t = "nagaram"
# Output: true
# Example 2:

# Input: s = "rat", t = "car"
# Output: false

#Solution 
# 1. Validate and make sure these are strings 
# 2. First we have to convert these strings into lower case
# 3. Make sure len of each string is equal, else false
# 4. Sort those string and if they are equal , return True , else False
# 5. If they matches then its a valid anagram 
# 6. Else it's not a valid anagram

import os 

def find_anagram(string1, string2 ):
    a=len(string1)
    b=len(string2)
    if a != b :
        return False
    elif (sorted(string1) == sorted(string2)):
        return True
    else:
        return False 
if __name__ == "__main__":
    string1=input("Enter the first String1: ".lower())
    string2=input("Enter the first String2: ".lower())
    if find_anagram(string1, string2):
        #print ("The" , string1, string2 , "are anagram" )
        print ("The {} and {} are anagram" .format(string1, string2))
    else:
        print ("The {} and {} are not anagram" .format(string1, string2) )