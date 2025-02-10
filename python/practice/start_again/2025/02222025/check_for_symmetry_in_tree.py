#   https://www.geeksforgeeks.org/recursion-on-trees-in-python/


class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
def is_Symmetric(left, right):
    if left is None and right is None:
        return True
    if left is None or right is None or left.value != right.value:
        return False
    return is_Symmetric(left.left, right.right) and is_Symmetric(left.right, right.left)
def check_symmetry(root):
    if root is None:
        return True 
    return is_Symmetric(root.left, root.right)

symmetric_root = TreeNode(1)
symmetric_root.left = TreeNode(2)
symmetric_root.right = TreeNode(2)
symmetric_root.left.left = TreeNode(3)
symmetric_root.left.right = TreeNode(4)
symmetric_root.right.left = TreeNode(4)
symmetric_root.right.right = TreeNode(3)

# Create a non-symmetric binary tree
non_symmetric_root = TreeNode(1)
non_symmetric_root.left = TreeNode(2)
non_symmetric_root.right = TreeNode(2)
non_symmetric_root.left.right = TreeNode(3)
non_symmetric_root.right.right = TreeNode(3)

# Check symmetry
print("Is the symmetric tree symmetric?", check_symmetry(symmetric_root))
print("Is the non-symmetric tree symmetric?", check_symmetry(non_symmetric_root))
