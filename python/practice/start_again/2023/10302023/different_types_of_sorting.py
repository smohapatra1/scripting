# #   https://leetcode.com/problems/sort-an-array/
#   https://leetcode.com/problems/sort-an-array/solutions/2162769/python3-5-common-sorting-algorithms-selection-bubble-insertion-merge-quick/

# 912. Sort an Array
# Medium
# 5.6K
# 723
# Companies
# Given an array of integers nums, sort the array in ascending order and return it.

# You must solve the problem without using any built-in functions in O(nlog(n)) time complexity and with the smallest space complexity possible.

 

# Example 1:

# Input: nums = [5,2,3,1]
# Output: [1,2,3,5]
# Explanation: After sorting the array, the positions of some numbers are not changed (for example, 2 and 3), while the positions of other numbers are changed (for example, 1 and 5).
# Example 2:

# Input: nums = [5,1,1,2,0,0]
# Output: [0,0,1,1,2,5]
# Explanation: Note that the values of nums are not necessairly unique.
 

from typing import List

def sortArray(self, nums: List[int]) -> List[int]:
    self.selectionSort(nums)
    #self.bubblesort(nums)
    #self.insertionsort(nums)
    #self.mergesort(nums)
    #self.quicksort(nums)
    #return nums

def selectionSort(nums):
    for i in range(len(nums)):
        min_idx=i
        for j in range(i, len(nums)):
            if nums[j] < nums[min_idx]:
                min_idx= j
        nums[i], nums[min_idx] = nums[min_idx], nums[i]
    return nums

def bubbleSort(nums):
    for i in range(len(nums)):
        swapped=False
        for j in range(len(nums)-i-1):
            if nums[j] > nums[j+1]:
                nums[j], nums[j+1] = nums[j+1], nums[j]
                swapped=True
        if not swapped:
            break
    return nums

def insertionSort(nums):
    for i in range(len(nums)):
        key=nums[i]
        j=i-1
        while j>=0 and key <nums[j]:
            nums[j+1] = nums[j]
            j-=1
        nums[j+1] = key 
    return nums

def mergeSort(nums):
    def merge(nums, L, R):
        i=j=k=0
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                nums[k] = L[i]
                i+=1
            else:
                nums[k] = R[j]
                j+=1
            k+=1
        while i < len(L):
            nums[k] = L[i]
            i+=1
            k+=1
        while j < len(R):
            nums[k] = R[j]
            j+=1
            k+=1
    if len(nums) > 1:
        mid=len(nums)//2
        L=nums[:mid]
        R=nums[mid:]
        mergeSort(L)
        mergeSort(R)
        merge(nums, L, R)
    return nums

import random
def quickSort(nums):
    def partition(l,r):
        pivot_idx=random.choice(range(l, r+1))
        pivot=nums[pivot_idx]
        left, move, right = l,l,r
        while move <=right:
            if nums[move]<pivot:
                nums[left], nums[move] = nums[move], nums[left]
                move +=1
                left +=1
            elif nums[move]> pivot:
                nums[right], nums[move] = nums[move], nums[right]
                right -=1
            else:
                move+=1
        return left-1, move

    def quicksort(nums, low, high):
        if low < high:
            l,r = partition(low, high)
            quicksort(nums, low, l)
            quicksort(nums, r, high)
        #return nums
    quicksort(nums, 0, len(nums)-1)
    return nums





if __name__ == "__main__":
    #nums=[5,2,3,1]
    nums = [5,1,1,2,0,0]
    #print ("The numbers post sorting - Selection Sort is {}".format(selectionSort(nums)))
    #print ("The numbers post sorting - Bubble Sort is {}".format(bubbleSort(nums)))
    #print ("The numbers post sorting - Insertion Sort is {}".format(insertionSort(nums)))
    #print ("The numbers post sorting - Merge Sort is {}".format(mergeSort(nums)))
    print ("The numbers post sorting - Quick Sort is {}".format(quickSort(nums)))
