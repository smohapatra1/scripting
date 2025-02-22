#   https://www.geeksforgeeks.org/python-program-to-search-an-element-in-a-circular-linked-list/


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
class CircularLinkedList:
    def __init__(self):
        self.head = Node(None)
        self.tail = Node(None)
        self.head.next = self.tail
        self.tail.next = self.head
    def add(self,data):
        newNode = Node(data)
        if self.head.data is None: 
            self.head = newNode
            self.tail = newNode 
            newNode.next = self.head
        else: 
            self.tail.next = newNode
            self.tail = newNode
            self.tail.next = self.head
    def findNode(self,element): 
        current = self.head
        i = 1
        f = 0     
        if(self.head == None): 
            print("Empty list")
        else: 
            while(True):
                if(current.data ==  element):
                    f += 1     
                    break
                current = current.next
                i = i + 1   
                if(current == self.head):     
                    break
            if(f > 0):     
                print("element is present")
            else:     
                print("element is not present")



if __name__ == "__main__":
    circularLinkedList = CircularLinkedList()
    circularLinkedList.add(1)
    circularLinkedList.add(2)
    circularLinkedList.add(3)
    circularLinkedList.add(4)
    circularLinkedList.add(5)
    circularLinkedList.add(6)
    circularLinkedList.add(7)
    circularLinkedList.findNode(2)
    circularLinkedList.findNode(8)
