#   https://www.geeksforgeeks.org/recursion-on-trees-in-python/

class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
def tree_size(node):
    if node is None:
        return 0 
    else:
        left_size = tree_size(node.left)
        right_size = tree_size(node.right)
        return left_size + right_size +1 

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.left = TreeNode(6)
root.right.right = TreeNode(7)
print ("Size of the tree: ", tree_size(root))