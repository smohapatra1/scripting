#   https://leetcode.com/problems/kth-smallest-element-in-a-bst/
# 230. Kth Smallest Element in a BST
# Medium

# Given the root of a binary search tree, and an integer k, return the kth smallest value (1-indexed) of all the values of the nodes in the tree.

 

# Example 1:


# Input: root = [3,1,4,null,2], k = 1
# Output: 1
# Example 2:


# Input: root = [5,3,6,2,4,null,null,1], k = 3
# Output: 3
 

def kth_smallest_bst(root):
    stack=[]
    res=[]
    while root or stack:
        while root:
            stack.append(root)
            root=root.left
        root=stack.pop()
        res.append(root)
        if len(res) == k:
            return res[-1].val
        root=root.right
    return res


if __name__ == "__main__":
    root = [3,1,4,2], 
    k = 1
    print ("{}".format(kth_smallest_bst(root)))