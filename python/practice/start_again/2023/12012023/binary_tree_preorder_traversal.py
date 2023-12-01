# #https://leetcode.com/problems/binary-tree-preorder-traversal/
# 144. Binary Tree Preorder Traversal
# Easy
# 7.6K
# 196
# Companies
# Given the root of a binary tree, return the preorder traversal of its nodes' values.

 

# Example 1:


# Input: root = [1,null,2,3]
# Output: [1,2,3]
# Example 2:

# Input: root = []
# Output: []
# Example 3:

# Input: root = [1]
# Output: [1]

from typing import List
def preOrder(root: List[int] )-> List[int]:
    head = root
    res = []
    stack = []
    while head or stack:
        if head:
            res.append(head.val)
            if head.right:
                stack.append(head.right)
            head = head.left
        else:
            head = stack.pop()
    return res

    

if __name__ == "__main__":
    root = [1,2,3]
    print ("{}".format(preOrder(root)))