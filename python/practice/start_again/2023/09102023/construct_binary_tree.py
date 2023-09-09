# 105. Construct Binary Tree from Preorder and Inorder Traversal
# Medium

# Given two integer arrays preorder and inorder where preorder is the preorder traversal of a binary tree and inorder is the inorder traversal of the same tree, construct and return the binary tree.
 

# Example 1:


# Input: preorder = [3,9,20,15,7], inorder = [9,3,15,20,7]
# Output: [3,9,20,null,null,15,7]
# Example 2:

# Input: preorder = [-1], inorder = [-1]
# Output: [-1]

import TreeNode 

def in_pre_order_bst(preorder, inorder):
    if not preorder:
        return None
    if not inorder:
        return None
    # Pop the first element in the preorder seq
    element=preorder.pop(0)
    root=TreeNode(element)
    idx=inorder.index(element)
    #Everything to the left of that node inorder goes to the left node
    root.left=in_pre_order_bst(preorder, inorder[:idx])
    #Everything to the right of root node inorder goes to the right of node
    root.right=in_pre_order_bst(preorder, inorder[idx+1:])
    return root

if __name__ == "__main__":
    preorder = [3,9,20,15,7]
    inorder = [9,3,15,20,7]
    print ("{}".format(in_pre_order_bst(preorder, inorder)))

