#   https://www.geeksforgeeks.org/python-program-for-reverse-a-linked-list/


class Node:
    def __init__ (self, data):
        self.data = data
        self.next = None
class LinkedList:
    def __init__ (self):
        self.head = None
    def reverse(self):
        prev = None
        current = self.head
        while current is not None:
            next = current.next
            current.next = prev 
            prev = current
            current = next
        self.head = prev 
    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node
    def printList(self):
        temp = self.head
        while temp:
            print (temp.data, end =" ")
            temp = temp.next


lilist = LinkedList()
lilist.push(20)
lilist.push(4)
lilist.push(15)
lilist.push(85)
print ("Given Linked List" )
lilist.printList()
lilist.reverse()
print ("\nReversed Linked List")
lilist.printList()