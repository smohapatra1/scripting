# #   https://leetcode.com/problems/minimum-distance-between-bst-nodes/
# 783. Minimum Distance Between BST Nodes
# Easy
# 3.4K
# 409
# Companies
# Given the root of a Binary Search Tree (BST), return the minimum difference between the values of any two different nodes in the tree.

 

# Example 1:


# Input: root = [4,2,6,1,3]
# Output: 1
# Example 2:


# Input: root = [1,0,48,null,null,12,49]
# Output: 1

def MinDistInBst(root: ListNode)-> int:
    self.ans = float('inf')
    self.prev = None
    self.inorder(root)
    return self.ans
def inorder(root: TreeNode)-> None:
    if root is None:
        return 
    self.inorder(root.left)
    if self.prev is not None:
        self.ans = min (self.ans, root.val - self.prev )
    self.prev = root.val
    self.inorder(root.right)


    

if __name__ == "__main__":
    root = [4,2,6,1,3]
    print ("{}".format(MinDistInBst(root)))