#   How Do You Reverse a Linked List?

class Node:
    def __init__ (self, data):
        self.data = data 
        self.next = None
class Linkedlist:
    def __init__ (self):
        self.head = None
    def reverse_list(head):
        prev = None
        while head:
            tmp = head.next
            head.next = prev 
            prev = head 
            head = tmp
        return prev
    if __name__ == "__main__":
        head = [ 1, 2,3, 4, 5 ]
        print ("Current input {} and reversed output {}".format(head, reverse_list(head)))


