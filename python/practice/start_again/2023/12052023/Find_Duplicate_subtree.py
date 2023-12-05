# #   https://leetcode.com/problems/find-duplicate-subtrees/
# 652. Find Duplicate Subtrees
# Medium
# 5.6K
# 444
# Companies
# Given the root of a binary tree, return all duplicate subtrees.

# For each kind of duplicate subtrees, you only need to return the root node of any one of them.

# Two trees are duplicate if they have the same structure with the same node values.

 

# Example 1:


# Input: root = [1,2,3,4,null,2,4,null,null,4]
# Output: [[2,4],[4]]
# Example 2:


# Input: root = [2,1,1]
# Output: [[1]]
# Example 3:


# Input: root = [2,2,2,3,null,3,null]
# Output: [[2,3],[3]]

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

import collections
from typing import Optional
from typing import List
from collections import defaultdict
def DuplicateSubtree( root: TreeNode ) -> List[TreeNode]:
    seen = collections.defaultdict(int)
    res = []
    def helper(node):
        if not node:
            return
        sub = tuple([helper(root.left), node.val, helper(root.right)])
        if sub in seen and seen[sub] ==1:
            res.append(node)
        seen[sub] +=1
        return sub
    helper(root)
    return res 

if __name__ == "__main__":
    root = [1,2,3,4,2,4,4]
    print ("{}".format(DuplicateSubtree(root)))