# #   https://leetcode.com/problems/symmetric-tree/
# 101. Symmetric Tree
# Easy
# 14.6K
# 349
# Companies
# Given the root of a binary tree, check whether it is a mirror of itself (i.e., symmetric around its center).

 

# Example 1:


# Input: root = [1,2,2,3,4,4,3]
# Output: true
# Example 2:


# Input: root = [1,2,2,null,3,null,3]
# Output: false
 
def symmetricTree( root: TreeNode) -> bool:
    if not root:
        return None
    return self.isSame(root.left, root.right)
def isSame(leftroot, rightroot):
    if leftroot == None and rightroot == None:
        return True
    if leftroot == None or rightroot == None:
        return False
    if leftroot.val != rightroot.val:
        return False
    return self.isSame(leftroot.left , rightroot.right) and self.isSame(leftroot.right, rightroot.left)


if __name__ == "__main__":
    root = [1,2,2,3,4,4,3]
    print ("{}".format(root))