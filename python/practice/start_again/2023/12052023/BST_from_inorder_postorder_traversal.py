# #   https://leetcode.com/problems/construct-binary-tree-from-inorder-and-postorder-traversal/


# 106. Construct Binary Tree from Inorder and Postorder Traversal
# Medium
# 7.7K
# 119
# Companies
# Given two integer arrays inorder and postorder where inorder is the inorder traversal of a binary tree and postorder is the postorder traversal of the same tree, construct and return the binary tree.

 

# Example 1:


# Input: inorder = [9,3,15,20,7], postorder = [9,15,7,20,3]
# Output: [3,9,20,null,null,15,7]
# Example 2:

# Input: inorder = [-1], postorder = [-1]
# Output: [-1]

from typing import List
def buildTree( inorder: List[int], postorder: List[int])-> TreeNode:
    if not inorder or not postorder:
        return None 
    root = TreeNode(postorder[-1])
    index = inorder.index(postorder[-1])
    root.left = self.buildTree( inorder[:index], postorder[:index])
    root.right = self.buildTree(inorder[index +1 :), postorder[index:-1])
    return root


if __name__ == "__main__":
    inorder = [9,3,15,20,7]
    postorder = [9,15,7,20,3]
    print ("{}".format(buildTree(inorder, postorder)))  