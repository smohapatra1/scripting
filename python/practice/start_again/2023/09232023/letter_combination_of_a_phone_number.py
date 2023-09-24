#   https://leetcode.com/problems/letter-combinations-of-a-phone-number/
# 17. Letter Combinations of a Phone Number
# Medium
# 17.2K
# 899
# Companies
# Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent. Return the answer in any order.

# A mapping of digits to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.


 

# Example 1:

# Input: digits = "23"
# Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]
# Example 2:

# Input: digits = ""
# Output: []
# Example 3:

# Input: digits = "2"
# Output: ["a","b","c"]

from typing import List
def lettercombination( digits: str) -> List[str]:
    result=[]
    if not digits:
        return []
    phone_map={
        '2' : 'abc',
        '3' : 'def',
        '4' : 'ghi',
        '5' : 'jkl',
        '6' : 'mno',
        '7' : 'pqrs',
        '8' : 'tuv',
        '9' : 'wxyz'
    }
    def backtrack(combinations, next_digits):
        if len(next_digits) ==0:
            result.append(combinations)
        else:
            for letter in phone_map[next_digits[0]]:
                backtrack(combinations + letter, next_digits[1:])
    backtrack("", digits)
    return result

if __name__ == "__main__":
    digits = "23"
    print ("{}".format(lettercombination(digits)))

