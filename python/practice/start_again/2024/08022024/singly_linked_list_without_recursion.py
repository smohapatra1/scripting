#   How Do You Reverse a Singly Linked List Without Recursion?

def reverse_list(head):
    new_head = None
    while head:
        head.next, head, new_head = new_head, head.next, head # look Ma, no temp vars!
    return new_head