#   https://www.geeksforgeeks.org/python-program-for-reverse-a-linked-list/

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
class LinkedList:
    def __init__(self):
        self.head = None
    def reverseUtils(self, curr, prev):
        if curr.next is None:
            self.head = curr
            curr.next = prev
            return
        next = curr.next
        curr.next = prev
        self.reverseUtils(next, curr)
    def reverse(self):
        if self.head is None:
            return
        self.reverseUtils(self.head, None)
    def push(self, new_data):
        new_Node = Node(new_data)
        new_Node.next = self.head
        self.head = new_Node
    def printList(self):
        temp = self.head
        while (temp):
            print (temp.data, end=" ")
            temp = temp.next    

llist = LinkedList() 
llist.push(8) 
llist.push(7) 
llist.push(6) 
llist.push(5) 
llist.push(4) 
llist.push(3) 
llist.push(2) 
llist.push(1) 

print("Given linked list") 
llist.printList() 
  
llist.reverse() 
  
print("\nReverse linked list") 
llist.printList() 