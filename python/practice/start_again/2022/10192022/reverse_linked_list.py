# Reverse linked list 

class node:
    def __init__ (self, data):
        self.data=data
        self.next_node=None

class LinkedList:
    def __init__(self):
        self.head=None
    def reverse(self):
        current_node=self.head
        previous_node=None
        next_node=None
        while current_node is not None:
            next_node=current_node.next_node
            current_node.next_node=previous_node
            previous_node=current_node
            current_node=next_node
        self.head = previous_node
    def push(self, new_data):
        new_node=node(new_data)
        new_node.next=self.head
        self.head=new_node
    def printlist(self):
        temp=self.head
        while(temp):
            print ( temp.data, end=" ")
            temp=temp.next_node



if __name__ == '__main__':
    llist=LinkedList()
    llist.push(20)
    llist.push(100)
    llist.push(15)
    llist.push(200)
    print ("Given Linked list: ")
    llist.printlist()
    llist.reverse()
    print ("\n Reverse Linked List: ")
    llist.printlist()
   
