# 23. Merge k Sorted Lists
# Hard
# You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.

# Merge all the linked-lists into one sorted linked-list and return it.

 

# Example 1:

# Input: lists = [[1,4,5],[1,3,4],[2,6]]
# Output: [1,1,2,3,4,4,5,6]
# Explanation: The linked-lists are:
# [
#   1->4->5,
#   1->3->4,
#   2->6
# ]
# merging them into one sorted list:
# 1->1->2->3->4->4->5->6
# Example 2:

# Input: lists = []
# Output: []
# Example 3:

# Input: lists = [[]]
# Output: []
import heapq
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def MergeK(Lists):
    ListNode.__lt__ = lambda self, other: self.val < other.val
    h=[]
    head=tail=ListNode(0)
    for i in lists:
        if i: heapq.heappush(h,i)
    while h:
        node=heapq.heappop(h)
        tail.next=node
        tail=tail.next
        if node.next:
            heapq.heappush(h, node.next)
    return head.next



if __name__ == "__main__":
    lists = [[1,4,5],[1,3,4],[2,6]]
    print ("{}".format(MergeK(lists)))