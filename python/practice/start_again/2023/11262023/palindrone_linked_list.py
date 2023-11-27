# #   https://leetcode.com/problems/palindrome-linked-list/
# 234. Palindrome Linked List
# Easy
# 15.5K
# 834
# Companies
# Given the head of a singly linked list, return true if it is a 
# palindrome
#  or false otherwise.

 

# Example 1:


# Input: head = [1,2,2,1]
# Output: true
# Example 2:


# Input: head = [1,2]
# Output: false

from typing import List
def reverse (head: LisNode) -> ListNode:
    prev_node=None
    while head:
        next_node = head.next
        head.next = prev_node
        prev_node = head
        head = next_node
    return prev_node
def palindromeList(head: ListNode ) -> ListNode:
    fast = slow = head
    while fast != None and fast.next != None:
        fast = fast.next.next
        slow = slow.next
    fast = head
    slow = reverse(slow)
    while slow !=None:
        if slow.val !=fast.val:
            return False
        fast = fast.next
        slow = slow.next    
    return True



if __name__ == "__main__":
    head = [1,2,2,1]
    print ("{}".format(palindromeList(head)))