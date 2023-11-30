# #   https://leetcode.com/problems/sort-list/
# 148. Sort List
# Medium
# 11K
# 319
# Companies
# Given the head of a linked list, return the list after sorting it in ascending order.

 

# Example 1:


# Input: head = [4,2,1,3]
# Output: [1,2,3,4]
# Example 2:


# Input: head = [-1,5,3,4,0]
# Output: [-1,0,3,4,5]
# Example 3:

# Input: head = []
# Output: []

def SortList(head: ListNode) -> ListNode:
    if not head or not head.next:
        return head
    slow = head 
    fast = head.next
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    mid = slow.next
    slow.next = None
    left = SortList(head)
    right = SortList(mid)
    dummy = ListNode(0)
    
    curr = dummy 
    while left and right:
        if left.val < right.val:
            curr.next = left 
            left = left.next
        else:
            curr.next = right
            right = right.next
        curr = curr.next
    curr.next =left or right 
    return dummy.next




if __name__ == "__main__":
    head = [4,2,1,3]
    print ("{}".format(SortList(head)))