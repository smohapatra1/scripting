# 124. Binary Tree Maximum Path Sum
# Hard

# A path in a binary tree is a sequence of nodes where each pair of adjacent nodes in the sequence has an edge connecting them. A node can only appear in the sequence at most once. Note that the path does not need to pass through the root.

# The path sum of a path is the sum of the node's values in the path.

# Given the root of a binary tree, return the maximum path sum of any non-empty path.

 

# Example 1:


# Input: root = [1,2,3]
# Output: 6
# Explanation: The optimal path is 2 -> 1 -> 3 with a path sum of 2 + 1 + 3 = 6.
# Example 2:


# Input: root = [-10,9,20,null,null,15,7]
# Output: 42
# Explanation: The optimal path is 15 -> 20 -> 7 with a path sum of 15 + 20 + 7 = 42.
 
def __init__(self):
    self.maxSum=float('-inf')
def maxPathSum(root):
    def traverse(root):
        if root:
            left=traverse(root.left)
            right=traverse(root.right)
            self.maxSum=max(self.maxSum,root.val,root.val +  left, root.val + right, root.val + left + right)
            return max(root.val, root.val + left.root.val + right)
        else:
            return 0
        traverse(root)
        return self.maxSum


if __name__ == "__main__":
    root=[1,2,3]
    print ("{}".format(maxPathSum(root)))