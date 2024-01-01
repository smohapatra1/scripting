# #   https://leetcode.com/problems/stickers-to-spell-word/
# 691. Stickers to Spell Word
# Hard
# 1.1K
# 87
# Companies
# We are given n different types of stickers. Each sticker has a lowercase English word on it.

# You would like to spell out the given string target by cutting individual letters from your collection of stickers and rearranging them. You can use each sticker more than once if you want, and you have infinite quantities of each sticker.

# Return the minimum number of stickers that you need to spell out target. If the task is impossible, return -1.

# Note: In all test cases, all words were chosen randomly from the 1000 most common US English words, and target was chosen as a concatenation of two random words.

 

# Example 1:

# Input: stickers = ["with","example","science"], target = "thehat"
# Output: 3
# Explanation:
# We can use 2 "with" stickers, and 1 "example" sticker.
# After cutting and rearrange the letters of those stickers, we can form the target "thehat".
# Also, this is the minimum number of stickers necessary to form the target string.
# Example 2:

# Input: stickers = ["notice","possible"], target = "basicbasic"
# Output: -1
# Explanation:
# We cannot form the target "basicbasic" from cutting letters from the given stickers.
 
from typing import List
from collections import Counter
def MinStickers(stickers: List[str], target: str) -> int:
    stickers=[Counter(s) for s in stickers if set(s)& set(target)]
    def generate(target):
        if not target: 
            return 0
        target_counter= Counter(target)
        res = float("inf")
        for sticker in stickers:
            if sticker[target[0]] == 0:
                continue
            tmp=1+generate("".join([letter*count for letter, count in (target_counter -sticker).items()]))
            res=min(res, tmp)
        return res
    res=generate(target)
    return -1 if res== float("inf") else res



if __name__ == "__main__":
    stickers = ["with","example","science"]
    target = "thehat"
    print ("{}".format(MinStickers(stickers, target)))