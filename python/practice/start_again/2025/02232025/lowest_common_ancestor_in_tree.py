#   https://www.geeksforgeeks.org/recursion-on-trees-in-python/

class TreeNode:
    def __init__ (self, value):
        self.value = value
        self.left = None
        self.right = None
def find_lca(root, node1, node2):
    if root is None:
        return None
    if root.value == node1 or root.value == node2:
        return root
    left_lca = find_lca(root.left, node1, node2)
    right_lca = find_lca(root.right, node1, node2)
    if left_lca and right_lca:
        return root
    return left_lca if left_lca else right_lca

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.left = TreeNode(6)
root.right.right = TreeNode(7)
node1 = 4 
node2 = 5 
lca_node = find_lca(root, node1, node2)
if lca_node:
    print (f"LCA of nodes {node1} and {node2} is : {lca_node.value}")
else:
    print (f"Nodes {node1} and {node2} are not found in the tree and they don't have a common ancestor")
