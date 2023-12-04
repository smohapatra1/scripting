# #   https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/

# 103. Binary Tree Zigzag Level Order Traversal
# Medium
# 10.3K
# 269
# Companies
# Given the root of a binary tree, return the zigzag level order traversal of its nodes' values. (i.e., from left to right, then right to left for the next level and alternate between).

 

# Example 1:


# Input: root = [3,9,20,null,null,15,7]
# Output: [[3],[20,9],[15,7]]
# Example 2:

# Input: root = [1]
# Output: [[1]]
# Example 3:

# Input: root = []
# Output: []

from typing import List
from collections import deque
def zigzacLevelOrder(root: TreeNode) -> List[List[int]]:
    if not root:
        return []
    queue = collections.deque([root])
    res =[]
    even_level = False
    while queue:
        n = len(queue)
        level = []
        for _ in range(n):
            node = queue.popleft()
            level.append(node.val)
            if node.left :
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        if even_level:
            res.append(level [::-1])
        else:
            res.append(level)
        even_level = not even_level
    return res



if __name__ == "__main__":
    root = [3,9,20,null,null,15,7]
    print ("{}".format(zigzacLevelOrder(root)))