#   https://www.geeksforgeeks.org/recursion-on-trees-in-python/

class TreeNode:
    def __init__ (self, value):
        self.value = value
        self.left = None
        self.right = None
def tree_height(node):
    if node is None:
        return 0 
    else:
        left_height = tree_height(node.left)
        right_height = tree_height(node.right)
        return max(left_height, right_height) +1 
def tree_depth(node):
    if node is None:
        return 0 
    else:
        left_depth = tree_depth(node.left)
        right_depth = tree_depth(node.right)
        return max(left_depth, right_depth) +1 

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.right = TreeNode(6)
root.right.left = TreeNode(7)
print ("Height of the tree", tree_height(root))
print ("Depth of the tree", tree_depth(root))