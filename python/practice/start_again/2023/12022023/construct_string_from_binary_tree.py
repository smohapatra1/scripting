# #   https://leetcode.com/problems/construct-string-from-binary-tree/
# 606. Construct String from Binary Tree
# Easy
# 2.7K
# 3.2K
# Companies
# Given the root of a binary tree, construct a string consisting of parenthesis and integers from a binary tree with the preorder traversal way, and return it.

# Omit all the empty parenthesis pairs that do not affect the one-to-one mapping relationship between the string and the original binary tree.

 

# Example 1:


# Input: root = [1,2,3,4]
# Output: "1(2(4))(3)"
# Explanation: Originally, it needs to be "1(2(4)())(3()())", but you need to omit all the unnecessary empty parenthesis pairs. And it will be "1(2(4))(3)"
# Example 2:


# Input: root = [1,2,3,null,4]
# Output: "1(2()(4))(3)"
# Explanation: Almost the same as the first example, except we cannot omit the first parenthesis pair to break the one-to-one mapping relationship between the input and the output.
 
def tree2Str(root: TreeNode) -> str:
    if root is None:
        return ""
    output : str = str(root.val)
    if (root.left != None or root.right != None):
        output +="( " + self.tree2Str(root.left) + ")"
    if (root.right != None):
        output +="("+ self.tree2Str(root.right) + ")"
    return output

if __name__ == "__main__":
    root = [1,2,3,4]
    print ("{}".format(tree2Str(root)))