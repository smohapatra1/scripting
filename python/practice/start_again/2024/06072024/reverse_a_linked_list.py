#    How do you reverse a Linked List?

class Node:

    # Constructor to initialize the node object
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    # Function to initialize head
    def __init__(self):
        self.head = None

    def reverse_list (head):
        prev = None
        while head:
            tmp = head.next
            head.next = prev 
            prev = head 
            head = tmp
        return prev    

    if __name__ == "__main__":
        head = [ 1, 2, 3, 4, 5 ]
        print ("Current input {} and Reversed Output {}".format(head, reverse_list(head)))