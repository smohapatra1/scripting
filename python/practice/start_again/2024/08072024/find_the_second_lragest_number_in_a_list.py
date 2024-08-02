#   Find the second largest number form a list 

def Second_Largest(nums):
    largest = float( '-inf' )
    second_largest = float( '-inf' )
    for i in nums:
        if i > largest:
            second_largest = largest
            largest = i 
        elif i > second_largest and i != largest:
            second_largest = i 
    return second_largest

if __name__ == "__main__":
    nums = [5, 2, 8, 1, 9]
    result = Second_Largest(nums)
    print (result)