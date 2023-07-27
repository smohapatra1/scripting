# 128. Longest Consecutive Sequence
# Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.
# You must write an algorithm that runs in O(n) time.

 
# Example 1:

# Input: nums = [100,4,200,1,3,2]
# Output: 4
# Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.
# Example 2:

# Input: nums = [0,3,7,2,5,8,4,6,0,1]
# Output: 9


# Method-01 - Leet code didn't accept it  
# Algorithm
# Initialize Empty array val and a variable c with value zero
# Iterate using a for loop between range zero to l with variable i
# Initialize a variable n with value 1
# Use a nested while loop until arr[i]+n in arr
# for each iteration increment the value of c & n by 1
# Append c+1 in val
# set value of c to 0
# print maximum of val

# 
# def longest_consecutive(arr, n ):
#     n=len(arr)
#     val=[]
#     c=0         # A variable 
#     for i in range(n):
#         l=1     # A new variable 
#         while arr[i] + l in arr:
#             c+=1
#             l+=1
#         val.append(c+1)
#         c=0
#     return max(val)



# Method-02 - 

# Visualize the problem on a number line after converting the array into a set
# Notice how the starting number of every sequence on a number line doesn't have a neighbor to the left of it?
# Set the length = 1 at the start of every sequence and iterate through instances of n+length using a while loop and at the end of the for loop iteration, set longest = max(length, maxlength)

def longest_consecutive(arr):
    seen = set(arr)
    longest =0 
    for n in seen:
        if (n-1) not in seen:
            length = 1 
            while ( n+length) in seen:
                length +=1
            longest = max ( length, longest)
    return longest




if __name__ == "__main__":
    arr=[7, 8, 1, 5, 4, 3]
    print ("The longest consecutive number {} from the list {}".format(longest_consecutive(arr),arr))