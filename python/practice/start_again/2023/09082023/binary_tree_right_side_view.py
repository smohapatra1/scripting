#   https://leetcode.com/problems/binary-tree-right-side-view/
# 199. Binary Tree Right Side View
# Medium

# Given the root of a binary tree, imagine yourself standing on the right side of it, return the values of the nodes you can see ordered from top to bottom.

 

# Example 1:


# Input: root = [1,2,3,null,5,null,4]
# Output: [1,3,4]
# Example 2:

# Input: root = [1,null,3]
# Output: [1,3]
# Example 3:

# Input: root = []
# Output: []

def RightSideView(root):
    def solve(root,level):
        res=[]
        if root:
            if len(res) == level:
                res.append(root.val)
            solve(root.right, level+1)
            solve(root.left, level+1)
        return
    
    solve(root,0)
    return res



if __name__ == "__main__":
    root = [1,2,3,5,4]
    print ("Right Side View is : {}".format(RightSideView(root)))