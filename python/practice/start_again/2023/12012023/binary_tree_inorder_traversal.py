# #   https://leetcode.com/problems/binary-tree-inorder-traversal/
# 94. Binary Tree Inorder Traversal
# Easy
# 12.6K
# 682
# Companies
# Given the root of a binary tree, return the inorder traversal of its nodes' values.

 

# Example 1:


# Input: root = [1,null,2,3]
# Output: [1,3,2]
# Example 2:

# Input: root = []
# Output: []
# Example 3:

# Input: root = [1]
# Output: [1]

from typing import List
def binaryTreeInOrder( root : List ) -> List:
    st = []
    res = []
    while root or st:
        while root:
            st.append(root)
            root = root.left
        root = st.pop()
        res.append(root.val)
        root = root.right
    return res


if __name__ == "__main__":
    root = [1,2,3]
    print ("{}".format(binaryTreeInOrder(root)))