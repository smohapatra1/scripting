# #   https://leetcode.com/problems/populating-next-right-pointers-in-each-node/
# 116. Populating Next Right Pointers in Each Node
# Medium
# 9.3K
# 286
# Companies
# You are given a perfect binary tree where all leaves are on the same level, and every parent has two children. The binary tree has the following definition:

# struct Node {
#   int val;
#   Node *left;
#   Node *right;
#   Node *next;
# }
# Populate each next pointer to point to its next right node. If there is no next right node, the next pointer should be set to NULL.

# Initially, all next pointers are set to NULL.

 

# Example 1:


# Input: root = [1,2,3,4,5,6,7]
# Output: [1,#,2,3,#,4,5,6,7,#]
# Explanation: Given the above perfect binary tree (Figure A), your function should populate each next pointer to point to its next right node, just like in Figure B. The serialized output is in level order as connected by the next pointers, with '#' signifying the end of each level.
# Example 2:

# Input: root = []
# Output: []

from collections import deque
def nextPointer(root: '[Node]') -> '[Node]':
    if not root:
        return None
    queue=collections.deque([root])
    while queue:
        size = len(queue)
        for i in range(size):
            node= queue.popleft()
            if i < size - 1 :
                node.next = queue[0]
                if node.left :
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
    return root





if __name__ == "__main__":
    root = [1,2,3,4,5,6,7]
    print ("{}".format(nextPointer(root)))

