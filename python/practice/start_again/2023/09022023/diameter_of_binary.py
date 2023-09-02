# 543. Diameter of Binary Tree
# Easy
# Given the root of a binary tree, return the length of the diameter of the tree.

# The diameter of a binary tree is the length of the longest path between any two nodes in a tree. This path may or may not pass through the root.

# The length of a path between two nodes is represented by the number of edges between them.

 

# Example 1:


# Input: root = [1,2,3,4,5]
# Output: 3
# Explanation: 3 is the length of the path [4,2,1,3] or [5,2,1,3].
# Example 2:

# Input: root = [1,2]
# Output: 1

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# class Solutions:
#     def __init__ (self):
#         self.diameter=0
#     def depth(node, root: Optional[TreeNode]) -> int:
#         left=self.depth(node.left) if node.left else 0
#         right=self.depth(node.right) if node.right else 0
#         if left + right > self.diameter:
#             self.diameter = left + right 
#         return 1 + (left if left > right else right)

#     def diameterOfBinaryTree(self, root : Optional[TreeNode]) -> int:
#         #if not root:
#         #    return 0
#         root = [1,2,3,4,5]
#         self.depth(root)
#         return self.diameter
#Solution-02
    def diameterOfBinaryTree(self, root : Optional[TreeNode]) -> int:
        diameter=0
        def depth(node, root : Optional[TreeNode]) -> int:
            nonlocal diameter
            if node is None:
                return 0
            left = depth(node.left)
            right= depth(node.right)
            diameter=max(diameter, left + right)
            return 1 + max(left, right)
        depth(root)
        return diameter
    
if __name__ == "__main__":
    root = [1,2,3,4,5]
    print ("{}".format(diameterOfBinaryTree( root)))
