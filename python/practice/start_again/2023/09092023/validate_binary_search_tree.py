#    https://leetcode.com/problems/validate-binary-search-tree/
# 98. Validate Binary Search Tree
# Medium
# 15.7K
# 1.3K
# Companies
# Given the root of a binary tree, determine if it is a valid binary search tree (BST).

# A valid BST is defined as follows:

# The left 
# subtree
#  of a node contains only nodes with keys less than the node's key.
# The right subtree of a node contains only nodes with keys greater than the node's key.
# Both the left and right subtrees must also be binary search trees.
 

# Example 1:


# Input: root = [2,1,3]
# Output: true
# Example 2:


# Input: root = [5,1,4,null,null,3,6]
# Output: false
# Explanation: The root node's value is 5 but its right child's value is 4.
 
import sys

def isValidBST(root):
    #Using maximum system integer to represent infinity
    INF=sys.maxsize
    def solve(node, lower, upper):
        if not node:
            return True
        if lower < node.val < upper:
            return solve(node.left, lower, node.val) and solve(node.right, node.val, upper)
        else:
            return False
    return solve(node=root, lower=-INF, upper=INF) 



if __name__ == "__main__":
    root = [5,1,4,3,6]
    print ("{}".format(isValidBST(root)))