#   https://leetcode.com/problems/binary-tree-level-order-traversal/

# 102. Binary Tree Level Order Traversal
# Medium

# Given the root of a binary tree, return the level order traversal of its nodes' values. (i.e., from left to right, level by level).

 

# Example 1:


# Input: root = [3,9,20,null,null,15,7]
# Output: [[3],[9,20],[15,7]]
# Example 2:

# Input: root = [1]
# Output: [[1]]
# Example 3:

# Input: root = []
# Output: []

def __init__(self, val=0, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right

def levelOrder(root):
    if not root:
        return []
    queue=[root]
    result=[]
    while queue:
        next_queue=[]
        level=[]
        for root in queue:
            level.append(root.val)
            if root.left:
                next_queue.append(root.left)
            if root.right:
                next_queue.append(root.right)
        result.append(level)
        queue=next_queue

    return result 


if __name__ == "__main__":
    root = [3,9,20,15,7]
    print ("{}".format(levelOrder(root)))
