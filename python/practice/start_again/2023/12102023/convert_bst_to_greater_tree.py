# #https://leetcode.com/problems/convert-bst-to-greater-tree/

# 538. Convert BST to Greater Tree
# Medium
# 5.1K
# 172
# Companies
# Given the root of a Binary Search Tree (BST), convert it to a Greater Tree such that every key of the original BST is changed to the original key plus the sum of all keys greater than the original key in BST.

# As a reminder, a binary search tree is a tree that satisfies these constraints:

# The left subtree of a node contains only nodes with keys less than the node's key.
# The right subtree of a node contains only nodes with keys greater than the node's key.
# Both the left and right subtrees must also be binary search trees.
 

# Example 1:


# Input: root = [4,1,6,0,2,5,7,null,null,null,3,null,null,null,8]
# Output: [30,36,21,36,35,26,15,null,null,null,33,null,null,null,8]
# Example 2:

# Input: root = [0,null,1]
# Output: [1,null,1]
 
class TreeNode:
    def __init__(self, val=0, left=None, next=None):
        self.val=val
        self.left=left
        self.next=next

def ConvertBST_GreaterTree( root: TreeNode) -> TreeNode:
    sum=0
    sol(root)
    return root
def sol(node):
    if not node:
        return
    sol(node.right)
    sum +=node.val
    node.val=sum
    sol(node.left)


if __name__ == "__main__":
    root = [4,1,6,0,2,5,7,null,null,null,3,null,null,null,8]
    print ("{}".format(ConvertBST_GreaterTree(root)))