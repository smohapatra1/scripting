# #   https://leetcode.com/problems/remove-linked-list-elements/
# 203. Remove Linked List Elements
# Easy
# 7.9K
# 221
# Companies
# Given the head of a linked list and an integer val, remove all the nodes of the linked list that has Node.val == val, and return the new head.

 

# Example 1:


# Input: head = [1,2,6,3,4,5,6], val = 6
# Output: [1,2,3,4,5]
# Example 2:

# Input: head = [], val = 1
# Output: []
# Example 3:

# Input: head = [7,7,7,7], val = 7
# Output: []

def removeLinkedList(head: ListNode, val: int )-> ListNode:
    dummy_node=ListNode(-1)
    dummy_node.next = head 
    current_node = dummy_node
    while current_node.next !=None:
        if current_node.next.val == val:
            current_node.next = current_node.next.next
        else:
            current_node = current_node.next
    return dummy_node.next

if __name__ == "__main__":
    head = [1,2,6,3,4,5,6]
    val = 6
    print ("{}".format(removeLinkedList(head, val )))