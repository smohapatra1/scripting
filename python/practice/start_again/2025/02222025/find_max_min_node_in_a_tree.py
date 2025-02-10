#   https://www.geeksforgeeks.org/recursion-on-trees-in-python/


class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
def find_max(node):
    if node is None:
        return float('-inf')
    else:
        max_left = find_max(node.left)
        max_right = find_max(node.right)
        return max(node.value, max_left, max_right)
def find_min(node):
    if node is None:
        return float('inf')
    else:
        min_left = find_min(node.left)
        min_right = find_min(node.right)
        return min(node.value, min_left, min_right)

root = TreeNode(5)
root.left = TreeNode(3)
root.right = TreeNode(7)
root.left.left = TreeNode(2)
root.left.right = TreeNode(4)
root.right.left = TreeNode(6)
root.right.right = TreeNode(8)

print ("Maximum element in the tree:", find_max(root))
print ("Minimum element in the tree:", find_min(root))
