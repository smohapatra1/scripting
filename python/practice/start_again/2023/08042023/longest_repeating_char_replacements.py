# 424. Longest Repeating Character Replacement

# You are given a string s and an integer k. You can choose any character of the string and change it to any other uppercase English character. You can perform this operation at most k times.

# Return the length of the longest substring containing the same letter you can get after performing the above operations.

 

# Example 1:

# Input: s = "ABAB", k = 2
# Output: 4
# Explanation: Replace the two 'A's with two 'B's or vice versa.
# Example 2:

# Input: s = "AABABBA", k = 1
# Output: 4
# Explanation: Replace the one 'A' in the middle with 'B' and form "AABBBBA".
# The substring "BBBB" has the longest repeating letters, which is 4.
# There may exists other ways to achieve this answer too.

def longest_repeat_char_replace(word, k ):
    #Solution - 01 
    # left = 0 
    # count= {}
    # max_count=0
    # max_length=0
    # for idx in range(len(word)):
    #     count[word[idx]] = count.get(word[idx],0 ) + 1 # Increment the count of current chars 
    #     max_count=max(max_count, count[word[idx]]) # Update the max count of any char seen so far 
    #     if idx - left + 1 - max_count >k:
    #         count[word[left]] -=1
    #         left +=1
    #     max_length=max(max_length, idx - left +1 )
    # return max_length

    #Solution 02
    
    max_count=0
    result=0
    count = collections.Counter()
    for i in range(len(word)):
        count[word[i]] +=1  # Increment the count of current chars 
        max_count = max (max_count, count[word[i]])
        if result - max_count < k:
            result+=1
        else:
            count[word[i-result]] -=1
    return result

if __name__ == "__main__":
    word="ABAB"
    #word="AABABBAAAA"
    k=1
    print ("The length of the longest string is {}".format(longest_repeat_char_replace(word, k )))
