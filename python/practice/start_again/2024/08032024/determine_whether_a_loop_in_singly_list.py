#   How Do You Determine Whether There Is a Loop in a Singly Linked List?

class ListNode(object):
    def __init__(self, x):
        self.value = x
        self.next = None

def LinkedNodeTest(n):
    head_node = ListNode(0)    # head node of the linked list
    end_node = head_node       # initially end == head
    for i in range(1, n+1):
        new_end_node = ListNode(i)    # create the new end
        end_node.next = new_end_node  # make current end point to new end node
        end_node = new_end_node       # move end var to new end
    return head_node