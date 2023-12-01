# #   https://leetcode.com/problems/reverse-linked-list-ii/
# 92. Reverse Linked List II
# Medium
# 11K
# 526
# Companies
# Given the head of a singly linked list and two integers left and right where left <= right, reverse the nodes of the list from position left to position right, and return the reversed list.

 

# Example 1:


# Input: head = [1,2,3,4,5], left = 2, right = 4
# Output: [1,4,3,2,5]
# Example 2:

# Input: head = [5], left = 1, right = 1
# Output: [5]

def ReverseLinkedList(head : ListNode, left : int, right: int) -> ListNode:
    if not  head or left == right:
        return head
    temp = ListNode(0, head )
    prev = temp
    for _ in range(left - 1 ):
        prev = prev.next
    current = prev.next
    for _ in range(right - left ):
        next_node = current.next
        current.next, next_node.next, prev.next = next_node.next, prev.next, next_node
    return temp.next 


if __name__ == "__main__":
    head = [1,2,3,4,5]
    left = 2
    right = 4
    print ("{}".format(ReverseLinkedList(head, left, right)))