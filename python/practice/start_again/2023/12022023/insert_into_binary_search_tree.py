# #   https://leetcode.com/problems/insert-into-a-binary-search-tree/
# 701. Insert into a Binary Search Tree
# Medium
# 5.5K
# 164
# Companies
# You are given the root node of a binary search tree (BST) and a value to insert into the tree. Return the root node of the BST after the insertion. It is guaranteed that the new value does not exist in the original BST.

# Notice that there may exist multiple valid ways for the insertion, as long as the tree remains a BST after insertion. You can return any of them.

 

# Example 1:


# Input: root = [4,2,7,1,3], val = 5
# Output: [4,2,7,1,3,5]
# Explanation: Another accepted tree is:

# Example 2:

# Input: root = [40,20,60,10,30,50,70], val = 25
# Output: [40,20,60,10,30,50,70,null,null,25]
# Example 3:

# Input: root = [4,2,7,1,3,null,null,null,null,null,null], val = 5
# Output: [4,2,7,1,3,5]

def insertIntoBST( root : TreeNode, val: int) -> TreeNode:
    # Solution - 01 
    # if not root:
    #     return TreeNode(val)
    # curr = None
    # next = root
    # while next:
    #     curr = next
    #     next = curr.left if val < curr.val else curr.right
    # if val < curr.val:
    #     curr.left = TreeNode(val)
    # else:
    #     curr.right = TreeNode(val)
    # return root

    # Solution - 02 
    if root is None:
        return TreeVal(val)
    if root.val < val:
        root.right = self.insertIntoBST(root.right.val)
    else:
        root.left = self.insertIntoBST(root.left.val)
    return root


if __name__ == "__main__":
    root = [4,2,7,1,3]
    val = 5
    print ("{}".format(root, val))