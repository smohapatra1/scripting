# #   https://leetcode.com/problems/middle-of-the-linked-list/
# 876. Middle of the Linked List
# Easy
# 10.7K
# 324
# Companies
# Given the head of a singly linked list, return the middle node of the linked list.

# If there are two middle nodes, return the second middle node.

 

# Example 1:


# Input: head = [1,2,3,4,5]
# Output: [3,4,5]
# Explanation: The middle node of the list is node 3.
# Example 2:


# Input: head = [1,2,3,4,5,6]
# Output: [4,5,6]
# Explanation: Since the list has two middle nodes with values 3 and 4, we return the second one.
 
def middleNode(head : ListNode) -> ListNode:
    temp = head 
    while temp and temp.next:
        head = head.next
        temp = temp.next.next
    return head

if __name__ == "__main__":
    head = [1,2,3,4,5]
    print ("{}".format(middleNode(head)))