#   https://www.geeksforgeeks.org/recursion-on-trees-in-python/

class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
def morris_traversal(root):
    current = root
    while current:
        if current.left is None:
            print (current.value , end = " ")
            current = current.right
        else:
            predecessor = current.left
            while predecessor.right and predecessor.right != current:
                predecessor = predecessor.right
            if predecessor.right is None:
                predecessor.right = current
                current = current.left
            else:
                predecessor.right = None
                print (current.value, end = " ")
                current = current.right
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
print("Morris In-order Traversal : ")
morris_traversal(root)
