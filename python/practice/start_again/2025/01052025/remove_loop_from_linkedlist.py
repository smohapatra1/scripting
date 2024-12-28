#   https://www.geeksforgeeks.org/problems/remove-loop-in-linked-list/1

class Node:
    def __init__ (self, x):
        self.data = x 
        self.next = None
def printList(cur):
    while cur:
        print (cur.data, end= ' ')
        cur = cur.next
    print ()
def removeLoop(head):
    nodeSet = set ()
    prev = None
    while head:
        if head in nodeSet:
            prev.next = None
            return
        nodeSet.add(head)
        prev = head 
        head = head.next
if __name__ == "__main__":
    head = Node(50)
    head.next = Node(20)
    head.next.next = Node(15)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(10)
    head.next.next.next.next.next = head.next.next
    removeLoop(head)
    printList(head)
