#   Can You Count How Many Leaf Nodes Are in a Given Binary Tree?

class BinaryTree:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def num_leaves(tree):
    count = 0 
    if tree.get_left() is None and tree.get_right() is None:
        count +=1
    if tree.get_left():
        count +=num_leaves(tree.get_left())
    if tree.get_right():
        count +=num_leaves(tree.get_right())
    return count

if __name__ == "__main__":
    a = BinaryTree(1)
    a.insert_left(2)
    a.insert_right(3)
    a.insert_right(4)
    a.get_right().insert_left(5)
    print(num_leaves(a))