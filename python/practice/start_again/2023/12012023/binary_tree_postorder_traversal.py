# #   https://leetcode.com/problems/binary-tree-postorder-traversal/
# 145. Binary Tree Postorder Traversal
# Easy
# 6.6K
# 183
# Companies
# Given the root of a binary tree, return the postorder traversal of its nodes' values.

 

# Example 1:


# Input: root = [1,null,2,3]
# Output: [3,2,1]
# Example 2:

# Input: root = []
# Output: []
# Example 3:

# Input: root = [1]
# Output: [1]

from typing import List
def postOrder(root: List[int]) -> List[int]:
    res=[]
    head = [root]
    while head:
        node = head.pop()
        res.append(node.val)
        if node.left:
            head.append(node.left)
        if node.right:
            head.append(node.right)
    return res [::-1]


if __name__ == "__main__":
    root = [1,2,3]
    print ("{}".format(postOrder(root)))