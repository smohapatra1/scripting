# #   https://leetcode.com/problems/swap-nodes-in-pairs/

# 24. Swap Nodes in Pairs
# Medium
# 11.4K
# 418
# Companies
# Given a linked list, swap every two adjacent nodes and return its head. You must solve the problem without modifying the values in the list's nodes (i.e., only nodes themselves may be changed.)

 

# Example 1:


# Input: head = [1,2,3,4]
# Output: [2,1,4,3]
# Example 2:

# Input: head = []
# Output: []
# Example 3:

# Input: head = [1]
# Output: [1]

from typing import List 
def swapNodes(head: ListNode) -> ListNode:
    temp = ListNode(None, head)
    prev = temp
    curr = head 
    while curr and curr.next:
        prev.next = curr.next
        curr.next = curr.next.next
        prev.next.next = curr
        prev, curr = curr, curr.next
    return temp.next
 


if __name__ == "__main__":
    head = [1,2,3,4]
    print ("{}".format(swapNodes(head)))
