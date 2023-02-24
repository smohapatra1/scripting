#Sliding Window technique - Getting the max sum

def MaxSum(arr, k ):
    size=len(arr)
    if size <=k:
        print ("Invalid Operations ")
        return -1 
    window_sum=sum([arr[i] for i in range(k)])
    max_sum=window_sum
    for i in range(size -k ):
        window_sum = max_sum - arr[i] + arr[i+k]
        max_sum=max(window_sum, max_sum)
    return max_sum
arr = [50,-10,90,200]
k = 2 #Values
answer=MaxSum(arr,k)
print (answer)