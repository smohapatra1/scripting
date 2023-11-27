# #   https://leetcode.com/problems/remove-duplicates-from-sorted-list/
# Given the head of a sorted linked list, delete all duplicates such that each element appears only once. Return the linked list sorted as well.

 

# Example 1:


# Input: head = [1,1,2]
# Output: [1,2]
# Example 2:


# Input: head = [1,1,2,3,3]
# Output: [1,2,3]
 
from typing import List
def remove_duplicate( head : ListNode) -> ListNode:
    curr = head
    while curr:
        while curr.next and curr.next.val == curr.val:
            curr.next = curr.next.next
        curr = curr.next
    return head

if __name__ == "__main__":
    head = [1,1,2]
    print ("{}".format(remove_duplicate(head)))