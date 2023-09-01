# 25. Reverse Nodes in k-Group
# Hard
# Given the head of a linked list, reverse the nodes of the list k at a time, and return the modified list.

# k is a positive integer and is less than or equal to the length of the linked list. If the number of nodes is not a multiple of k then left-out nodes, in the end, should remain as it is.

# You may not alter the values in the list's nodes, only nodes themselves may be changed.

 

# Example 1:


# Input: head = [1,2,3,4,5], k = 2
# Output: [2,1,4,3,5]
# Example 2:


# Input: head = [1,2,3,4,5], k = 3
# Output: [3,2,1,4,5]

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def Reverse(head,k):
    curr=head
    for _ in range(k):
        if not curr:
            return head
        curr=curr.next
        prev=None
        curr = head
        for _ in range(k):
            nxt=next.curr
            curr.next=prev
            prev=curr
            curr = nxt
        head.next=Reverse( head, k )
        return prev
         


if __name__ == "__main__":
    head = [1,2,3,4,5]
    k = 2
    print ("Input {} and Output {}".format(head, Reverse(head, k )))