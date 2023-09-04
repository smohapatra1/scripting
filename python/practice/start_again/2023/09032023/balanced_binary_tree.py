
# 110. Balanced Binary Tree
# Easy
# 9.8K
# 554
# Companies
# Given a binary tree, determine if it is 
# height-balanced
# .

 

# Example 1:


# Input: root = [3,9,20,null,null,15,7]
# Output: true
# Example 2:


# Input: root = [1,2,2,3,3,null,null,4,4]
# Output: false
# Example 3:

# Input: root = []
# Output: true




def isBalanced(root):
    return (Height(root) >=0 )
def Height(root):
    if root is None:
        return 0 
    leftheight=Height(root.left)
    rightheight=Height(root.right)
    if leftheight < 0 or rightheight < 0 or abs(leftheight - rightheight) > 1:
        return -1
    return max(leftheight , rightheight) +1




if __name__ == "__main__":
    root = [3,9,20,15,7]
    print ("{}".format(isBalanced(root)))