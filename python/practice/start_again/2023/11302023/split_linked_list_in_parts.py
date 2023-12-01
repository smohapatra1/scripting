# #https://leetcode.com/problems/split-linked-list-in-parts/
# 725. Split Linked List in Parts
# Medium
# 3.8K
# 299
# Companies
# Given the head of a singly linked list and an integer k, split the linked list into k consecutive linked list parts.

# The length of each part should be as equal as possible: no two parts should have a size differing by more than one. This may lead to some parts being null.

# The parts should be in the order of occurrence in the input list, and parts occurring earlier should always have a size greater than or equal to parts occurring later.

# Return an array of the k parts.

 

# Example 1:


# Input: head = [1,2,3], k = 5
# Output: [[1],[2],[3],[],[]]
# Explanation:
# The first element output[0] has output[0].val = 1, output[0].next = null.
# The last element output[4] is null, but its string representation as a ListNode is [].
# Example 2:


# Input: head = [1,2,3,4,5,6,7,8,9,10], k = 3
# Output: [[1,2,3,4],[5,6,7],[8,9,10]]
# Explanation:
# The input has been split into consecutive parts with size difference at most 1, and earlier parts are a larger size than the later parts.
 
def SplitToParts( head : ListNode, k: int) -> ListNode:
    length=0 
    temp = head 
    while temp:
        length +=1
        temp = temp.next
    part_size = length//k
    extra = length % k
    result = []
    temp = head 
    for i in range(k):
        result.append(temp)
        curr_part_size = part_size + 1 if extra > 0 else part_size
        extra -=1 
        for j in range(curr_part_size -1):
            temp = temp.next
        if temp:
            temp.next, temp = Node, temp.next
    return result

if __name__ == "__main__":
    head = [1,2,3,4,5,6,7,8,9,10]
    k = 3
    print ("{}".format(head, k ))
