#   https://www.geeksforgeeks.org/python-stack-using-doubly-linked-list/


class Node:
    def __init__ (self, data):
        self.data = data
        self.next = None
        self.prev = None
class Stack:
    def __init__(self):
        self.head = None
    def push(self, data):
        if self.head is None:
            self.head = Node(data)
        else:
            new_node = Node(data)
            self.head.prev = new_node
            new_node.next = self.head
            new_node.prev = None
            self.head = new_node
    def pop(self):
        if self.head.next is None:
            return None 
        elif self.head.next is None:
            temp = self.head.data
            self.head = None
            return temp
        else:
            temp = self.head.data
            self.head = self.head.next
            self.head.prev = None
            return temp
    def top(self):
        return self.head.data
    def size(self):
        temp = self.head
        count = 0 
        while temp is not None:
            count = count +1 
            temp = temp.next
        return count
    def isEmpty(self):
        if self.head is None:
            return True
        else:
            return False
    def printstack(self):
        print ("stack elements are :")
        temp = self.head
        while temp is not None:
            print (temp.data, end = " ")
            temp= temp.next

if __name__ == "__main__":
    stack = Stack()
    print ("Stack Operations using Doubly LinkedList")
    stack.push(4)
    stack.push(5)
    stack.push(6)
    stack.push(7)
    stack.printstack()
    print ("Top element is : ", stack.top())
    print ("Size of the stack : ", stack.size())
    stack.pop()
    stack.printstack()
    print ("\n Stack is empty ", stack.isEmpty())

