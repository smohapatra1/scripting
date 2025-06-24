#   https://search.brave.com/search?q=You+are+given+a+binary+tree.+Can+you+in-place+convert+it+into+a+doubly-linked+list+in+python&source=web&summary=1&conversation=61746167777fc838f404ae


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def convert_tree_to_list(node):
    if node is None:
        return
    convert_tree_to_list(node.left)
    if convert_tree_to_list.prev is None:
        convert_tree_to_list.head = node
    else:
        node.left = convert_tree_to_list.prev
        convert_tree_to_list.prev.right = node
    convert_tree_to_list.prev = node
    convert_tree_to_list(node.right)
def b_to_dll(root):
    if root is None:
        return root
    convert_tree_to_list.prev = None
    convert_tree_to_list.head = None
    convert_tree_to_list(root)
    while convert_tree_to_list.head.left:
        convert_tree_to_list.head = convert_tree_to_list.left
    return convert_tree_to_list.head