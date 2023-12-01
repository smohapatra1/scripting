# #   https://leetcode.com/problems/rotate-list/
# 61. Rotate List
# Medium
# 9.1K
# 1.4K
# Companies
# Given the head of a linked list, rotate the list to the right by k places.

 

# Example 1:


# Input: head = [1,2,3,4,5], k = 2
# Output: [4,5,1,2,3]
# Example 2:


# Input: head = [0,1,2], k = 4
# Output: [2,0,1]

def rotateList(head: ListNode, k: int ) -> ListNode:
    if not head or not k:
        return head 
    last = head 
    Length = 1 
    while last.next:
        last = last.next
        Length +=1
    last.next = head
    for _ in range(Length - k % Length):
        last = last.next
    temp = last.next
    last.next = None
    return temp




if __name__ == "__main__":
    head = [1,2,3,4,5]
    k = 2
    print ("{}".format(rotateList(head, k)))