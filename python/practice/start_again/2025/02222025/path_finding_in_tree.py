#   https://www.geeksforgeeks.org/recursion-on-trees-in-python/

class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None  
def find_path(root, target, path=None):
    if path is None:
        path = []
    if root is None:
        return []
    path.append(root.value)
    if root.value == target:
        return path
    left_path = find_path(root.left, target, path.copy())
    right_path = find_path(root.right, target, path.copy())
    if left_path:
        return left_path
    elif right_path:
        return right_path
    else:
        return []

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.left = TreeNode(6)
root.right.right = TreeNode(7)
target_node = 5
path_to_node = find_path(root, target_node)
if path_to_node:
    print(f"Path to node {target_node}: {path_to_node}")
else:
    print(f"Node {target_node} not found in the tree.")