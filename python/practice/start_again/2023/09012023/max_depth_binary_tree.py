# 104. Maximum Depth of Binary Tree
# Easy

# Given the root of a binary tree, return its maximum depth.

# A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

 

# Example 1:


# Input: root = [3,9,20,null,null,15,7]
# Output: 3
# Example 2:

# Input: root = [1,null,2]
# Output: 2



def maxDepth(root):
    def dfs(root, depth):
        if not root:
            return depth
        return (max(dfs(root.left, depth+1), dfs(root.right, depth+1)))
    return dfs(root, 0)


if __name__ == "__main__":
    root = [3,9,20,15,7]
    print ("Max Depth is {}".format(maxDepth(root)))