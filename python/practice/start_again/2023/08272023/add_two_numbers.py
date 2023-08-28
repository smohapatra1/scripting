# 2. Add Two Numbers
# Medium
# 27.9K
# 5.4K
# Companies
# You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

# You may assume the two numbers do not contain any leading zero, except the number 0 itself.

 

# Example 1:


# Input: l1 = [2,4,3], l2 = [5,6,4]
# Output: [7,0,8]
# Explanation: 342 + 465 = 807.
# Example 2:

# Input: l1 = [0], l2 = [0]
# Output: [0]
# Example 3:

# Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
# Output: [8,9,9,9,0,0,0,1]
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def AddNumbers(l1: ListNode, l2: ListNode):
    sumValue=0
    result = cur = ListNode(0)
    while l1 or l2 or sumValue:
        if l1:sumValue +=l1.val; l1=l1.next
        if l2:sumValue +=l2.val; l2=l2,next
        cur.next = cur = ListNode(sumValue % 10 )
        sumValue //=10
    return result.next



if __name__ == "__main__":
    l1 = [2,4,3]
    l2 = [5,6,4]
    print ("SumValue = {}".format(AddNumbers(l1, l2)))