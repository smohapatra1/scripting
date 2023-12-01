# #   https://leetcode.com/problems/insertion-sort-list/

# 147. Insertion Sort List
# Medium
# 3K
# 850
# Companies
# Given the head of a singly linked list, sort the list using insertion sort, and return the sorted list's head.

# The steps of the insertion sort algorithm:

# Insertion sort iterates, consuming one input element each repetition and growing a sorted output list.
# At each iteration, insertion sort removes one element from the input data, finds the location it belongs within the sorted list and inserts it there.
# It repeats until no input elements remain.
# The following is a graphical example of the insertion sort algorithm. The partially sorted list (black) initially contains only the first element in the list. One element (red) is removed from the input data and inserted in-place into the sorted list with each iteration.


 

# Example 1:


# Input: head = [4,2,1,3]
# Output: [1,2,3,4]
# Example 2:


# Input: head = [-1,5,3,4,0]
# Output: [-1,0,3,4,5]
 
def InsertionSortList( head : ListNode ) -> ListNode:
    
    temp = ListNode(0)
    curr = head
    while curr:
        tempcurr = curr
        while tempcurr.next and curr.val >=tempcurr.next.val:
            tempcurr = tempcurr.next
        tmp, tempcurr.next = tempcurr.next, curr
        curr = curr.next
        tempcurr.next.next = tmp
    return temp.next
        
        

if __name__ == "__main__":
     head = [4,2,1,3]
     print ("{}".format(InsertionSortList(head)))