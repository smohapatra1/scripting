# #   https://leetcode.com/problems/partition-list/

# 86. Partition List
# Medium
# 7K
# 800
# Companies
# Given the head of a linked list and a value x, partition it such that all nodes less than x come before nodes greater than or equal to x.

# You should preserve the original relative order of the nodes in each of the two partitions.

 

# Example 1:


# Input: head = [1,4,3,2,5,2], x = 3
# Output: [1,2,2,4,3,5]
# Example 2:

# Input: head = [2,1], x = 2
# Output: [1,2]
 
def PartitionList(head: ListNode, x:int  ) -> ListNode:
    before = ListNode(0)
    after = ListNode(0)
    before_curr = before
    after_curr = after
    while head:
        if head.val < x:
            before_curr.next, before_curr = head, head 
        else:
            after_curr.next, after_curr = head, head 
        head = head.next
    after_curr.next = None
    before_curr.next = after.next
    return before.next

if __name__ == "__main__":
    head = [1,4,3,2,5,2]
    x = 3
    print ("{}".format(PartitionList(head, x)))