# 347. Top K Frequent Elements
# Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.
#Ref https://interviewing.io/questions/top-k-frequent-elements 

# Example 1:

# Input: nums = [1,1,1,2,2,3], k = 2
# Output: [1,2]

#   Approach :- 
#   Accept the array of integers
#   Loop through the integers
#   Use counters 

#BFM
def top_k(nums,k):
    counts={}
    for num in nums:
        if num not in counts:
            counts[num] = 1 
        else:
            counts[num] +=1
        # Sort in descending order based on the counts
        counts_list=sorted(counts.items(), key=lambda x:x[1], reverse=True)
        sorted_counts=dict(counts_list[:k])
    return [num for num in sorted_counts]

if __name__ == "__main__":
    nums=[1,2,3,4,5,1,2,4,4,4,4]
    k=5 # Highest number of repeated numbers to show 
    print("Current numbers {}".format(nums))
    print("Most frequent number is {}".format(top_k(nums,k)))