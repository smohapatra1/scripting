# https://search.brave.com/search?q=Can+you+print+the+given+binary+tree%27s+nodes+level+by+level%2C+i.e.%2C+print+all+nodes+of+level+1+first%2C+then+level+2%2C+and+so+on%3F+using+python&source=web&summary=1&conversation=1e00d7642068f647894d29

from collections import deque
class Node:
    def __init__(self,value):
        self.value = value 
        self.left = None
        self.right = None
def print_level_order(root):
    if root is None:
        return
    queue = deque()
    queue.append(root)

    while queue:
        level_size = len(queue)
        for _ in range(level_size):
            node = queue.popleft()
            print(node.value, end=" ")
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        print()

if __name__ == "__main__":
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.left = Node(6)
    root.right.right = Node(7)
    print_level_order(root)