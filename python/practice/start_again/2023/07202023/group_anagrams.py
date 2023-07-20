# Given an array of strings strs, group the anagrams together. You can return the answer in any order.

# An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.


# Example 1:

# Input: strs = ["eat","tea","tan","ate","nat","bat"]
# Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

#   Idea 
#   Enter the arrays 
#   Create a dictionary 
#   Loop through each word
#   Break the words and sort them with Join
#   If word exists, append  the word to the value list of the corresponding keys
#   if key doesn't exist create a new key with sorted word 
#   After iterating through all the words, return the values of the dictionary as a list of lists with groups   


def groupAnagram(words):
    anagram_dict={}
    for word in words:
        sorted_word=''.join(sorted(word))
        if sorted_word in anagram_dict:
            anagram_dict[sorted_word].append(word)
        else:
            anagram_dict[sorted_word]=[word]
    return list(anagram_dict.values())

if __name__ == "__main__":
    words=["eat","tea","tan","ate","nat","bat"]
    n=len(words)
    print("The original list {}".format(words))
    print("The formatted list {}".format(groupAnagram(words)))