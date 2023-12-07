# # https://leetcode.com/problems/find-bottom-left-tree-value/
# 513. Find Bottom Left Tree Value
# Medium
# 3.2K
# 255
# Companies
# Given the root of a binary tree, return the leftmost value in the last row of the tree.

 

# Example 1:


# Input: root = [2,1,3]
# Output: 1
# Example 2:


# Input: root = [1,2,3,4,null,5,6,null,null,7]
# Output: 7

class TreeNode:
    def __init__ (self, val=0, left=None, next=None):
        self.val = val
        self.next=next
        self.left=left

from collections import deque
def find_bottom_left_tree( root: TreeNode) -> int:
    queue = deque([root])
    left_val = root.val
    while queue:
        size=len(queue)
        for i in range(size):
            node = queue.popleft()
            if i == 0:
                left_val = node.val
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
    return left_val



if __name__ == "__main__":
    root = [2,1,3]
    print ("{}".format(find_bottom_left_tree(root)))