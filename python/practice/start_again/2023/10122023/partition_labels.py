# #   https://leetcode.com/problems/partition-labels/

# 763. Partition Labels
# Medium
# 9.9K
# 365
# Companies
# You are given a string s. We want to partition the string into as many parts as possible so that each letter appears in at most one part.

# Note that the partition is done so that after concatenating all the parts in order, the resultant string should be s.

# Return a list of integers representing the size of these parts.

 

# Example 1:

# Input: s = "ababcbacadefegdehijhklij"
# Output: [9,7,8]
# Explanation:
# The partition is "ababcbaca", "defegde", "hijhklij".
# This is a partition so that each letter appears in at most one part.
# A partition like "ababcbacadefegde", "hijhklij" is incorrect, because it splits s into less parts.
# Example 2:

# Input: s = "eccbbbbdec"
# Output: [10]

from typing import List 
def partition_labels( s: str) -> List[int]:
    last_position_char={}
    for idx, char in enumerate(s):
        last_position_char[char]=idx
    start=0
    partition_length=[]
    last_position=0
    for idx, char in enumerate(s):
        last_position=max(last_position, last_position_char[char])
        if idx== last_position:
            curr_partition_length = last_position - start +1
            partition_length.append(curr_partition_length)
            start = idx +1
    return partition_length
if __name__ == "__main__":
    #s = "ababcbacadefegdehijhklij"
    s = "eccbbbbdec"
    print ("{}".format(partition_labels(s)))



