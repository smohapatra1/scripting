# #   https://www.hackerrank.com/challenges/one-month-preparation-kit-reverse-a-linked-list/problem?isFullScreen=true&h_l=interview&playlist_slugs%5B%5D=preparation-kits&playlist_slugs%5B%5D=one-month-preparation-kit&playlist_slugs%5B%5D=one-month-week-three
# Given the pointer to the head node of a linked list, change the next pointers of the nodes so that their order is reversed. The head pointer given may be null meaning that the initial list is empty.

# Example
#  references the list 

# Manipulate the  pointers of each node in place and return , now referencing the head of the list .

# Function Description

# Complete the reverse function in the editor below.

# reverse has the following parameter:

# SinglyLinkedListNode pointer head: a reference to the head of a list
# Returns

# SinglyLinkedListNode pointer: a reference to the head of the reversed list
# Input Format

# The first line contains an integer , the number of test cases.

# Each test case has the following format:

# The first line contains an integer , the number of elements in the linked list.
# Each of the next  lines contains an integer, the  values of the elements in the linked list.

# Constraints

# , where  is the  element in the list.
# Sample Input

# 1
# 5
# 1
# 2
# 3
# 4
# 5
# Sample Output

# 5 4 3 2 1 
# Explanation

# The initial linked list is: .

# The reversed linked list is: .

#!/bin/python3

import math
import os
import random
import re
import sys

class SinglyLinkedListNode:
    def __init__(self, node_data):
        self.data = node_data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_node(self, node_data):
        node = SinglyLinkedListNode(node_data)
        if not self.head:
            self.head = node
        else:
            self.tail.next = node
        self.tail = node


#
# Complete the 'reverse' function below.
#
# The function is expected to return an INTEGER_SINGLY_LINKED_LIST.
# The function accepts INTEGER_SINGLY_LINKED_LIST llist as parameter.
#

#
# For your reference:
#
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
#
#

def reverse(llist):
    # Write your code here
    prev=None
    current=llist
    while current:
        next_node=current.next
        current.next=prev
        prev=current
        current=next_node
    llist=prev
    return llist

if __name__ == '__main__':
    tests = int(input())
    for tests_itr in range(tests):
        llist_count = int(input())
        llist = SinglyLinkedList()
        for _ in range(llist_count):
            llist_item = int(input())
            llist.insert_node(llist_item)
        llist1 = reverse(llist.head)
    print (llist1)