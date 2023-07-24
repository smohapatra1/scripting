# 347. Top K Frequent Elements
# Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.

#Using Heap - It is not complete 

import heapq
from collections import Counter

def top_k_element(nums,k):
    counts=Counter(nums)
    min_heap = []
    for element, frequency in counts.items():
        heappush(min_heap, (frequency, element))
        if len(min_heap) > k:
            heappop(min_heap)
    return [num for (count ,num) in min_heap]

if __name__ == "__main__":
    nums=[1,2,3,4,1,1,1,12,1,1,1,2,4,4,4]
    k=2
    print ("Current numbers {} and {}".format(nums,k))
    print ("Most repeated numbers are {}".format(top_k_element(nums,k)))