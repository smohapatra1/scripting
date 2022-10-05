# Finding the middle node in a linked list overview 
class middle:
    def __init__(self,data):
        self.data=data
        self.next_node=None
class Node:
    def __init__(self,data):
        self.data=data
        self.next_node=None

class Linked_list:
    def __init__(self):
        self.head=None
        self.size=0
    def get_middle_node(self):
        fast_pointer=self.head
        slow_pointer=self.head
        while fast_pointer.next_node and fast_pointer.next_node.next_node: 
            fast_pointer=fast_pointer.next_node.next_node
            slow_pointer=slow_pointer.next.node
        return slow_pointer

    def insert(self, data):
        self.size=self.size +1
        new_node=Node(data)
        if not self.head:
            self.head = new_node
        else:
            new_node.next_node = self.head
            self.head=new_node

    if __name__ == '__main__':
        linked_list = Linked_List()
        linked_list.insert(10)
        linked_list.insert(20)
        linked_list.insert(10)

        print (linked_list.get_middle_node().data)

