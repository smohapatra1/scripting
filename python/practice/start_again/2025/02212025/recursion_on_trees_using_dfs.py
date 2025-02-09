#   https://www.geeksforgeeks.org/recursion-on-trees-in-python/


class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
def dfs_recursive(node):
    if node is None:
        return
    print (node.value)
    dfs_recursive(node.left)
    dfs_recursive(node.right)

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.left = TreeNode(6)
root.right.right = TreeNode(7)
print ("DFS Recursive ")
dfs_recursive(root)