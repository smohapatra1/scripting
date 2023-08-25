# 21. Merge Two Sorted Lists
# Easy

# You are given the heads of two sorted linked lists list1 and list2.

# Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.

# Return the head of the merged linked list.

 

# Example 1:


# Input: list1 = [1,2,4], list2 = [1,3,4]
# Output: [1,1,2,3,4,4]
# Example 2:

# Input: list1 = [], list2 = []
# Output: []
# Example 3:

# Input: list1 = [], list2 = [0]
# Output: [0]
import random
from typing import Optional
from typing import List
from typing import Any

def MergeList(list1, list2):
    #Solution-01

    # return sorted( list1 + list2 )

    #Solution-02
    
    l1=len(list1)
    l2=len(list2)
    result=[]
    i=j=0
    while i < l1 and j < l2:
        if list1[i] < list2[j]:
            result.append(list1[i])
            i+=1
        else:
            result.append(list2[j])
            j+=1
    result=result + list1[i:] + list2[j:]
    return result
     

if __name__ == "__main__":
    list1 = [1,2,4]
    list2 = [1,3,4]
    # list1 = []
    # list2 = []
    #MergeList(list1, list2)
    print ("Merge list are {}".format(MergeList(list1, list2)))