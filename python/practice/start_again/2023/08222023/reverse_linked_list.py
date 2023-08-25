# 206. Reverse Linked List
# Easy

# Given the head of a singly linked list, reverse the list, and return the reversed list.

 

# Example 1:


# Input: head = [1,2,3,4,5]
# Output: [5,4,3,2,1]
# Example 2:


# Input: head = [1,2]
# Output: [2,1]
# Example 3:

# Input: head = []
# Output: []

import os 
def reverse(head):
    if head is None or head.next is None:
        return head
    # #Iterative Approach 
    prev=None
    while head:
        next=head.next  # Initialize the next pointer 
        head.next=prev  # Assign previous pointer to curr next pointer 
        prev = head     # Assign current to prev
        head=next       # Assign next to current 
    return prev         # Return the previous pointer 

if __name__ == "__main__":
    head = [1,2,3,4,5]
    print ("Current input {} and Revered Output {}".format(head, reverse(head)))