#   https://www.google.com/search?q=You+are+given+an+unsorted+array+of+non-negative+integers+and+an+integer+sum.+Can+you+find+a+continuous+subarray+that+adds+to+a+given+sum%3F+using+python&client=safari&sca_esv=ccb8066356fd07b7&rls=en&sxsrf=AE3TifMmKarYPJTnL6epv7eV8c2S_1FNgA%3A1751566999123&ei=l8pmaLOlB9XJkPIPu9bmwAs&ved=0ahUKEwjzzKHGp6GOAxXVJEQIHTurGbgQ4dUDCBE&uact=5&oq=You+are+given+an+unsorted+array+of+non-negative+integers+and+an+integer+sum.+Can+you+find+a+continuous+subarray+that+adds+to+a+given+sum%3F+using+python&gs_lp=Egxnd3Mtd2l6LXNlcnAilgFZb3UgYXJlIGdpdmVuIGFuIHVuc29ydGVkIGFycmF5IG9mIG5vbi1uZWdhdGl2ZSBpbnRlZ2VycyBhbmQgYW4gaW50ZWdlciBzdW0uIENhbiB5b3UgZmluZCBhIGNvbnRpbnVvdXMgc3ViYXJyYXkgdGhhdCBhZGRzIHRvIGEgZ2l2ZW4gc3VtPyB1c2luZyBweXRob25IAFAAWABwAHgBkAEAmAEAoAEAqgEAuAEDyAEA-AEC-AEBmAIAoAIAmAMAkgcAoAcAsgcAuAcAwgcAyAcA&sclient=gws-wiz-serp

def find_subarray_with_sum(arr, target_sum):
    n = len(arr)
    current_sum = 0 
    start_index = 0 
    for i in range(n):
        current_sum += arr[i]
        while current_sum > target_sum and start_index <= i :
            current_sum -= arr[start_index]
            start_index +=1
        if current_sum == target_sum:
            print (f"Subarray found between indices {start_index} and {i}")
            return True
    print ("No Subarray found with the given num ")
    return False
    
arr1 = [15, 2, 4, 8, 9, 5, 10, 23]
sum1 = 23
find_subarray_with_sum(arr1, sum1)

arr2 = [1, 2, 3, 7, 5]
sum2 = 12
find_subarray_with_sum(arr2, sum2)

arr3 = [1, 2, 3, 4, 5]
sum3 = 15
find_subarray_with_sum(arr3, sum3)

arr4 = [10, 2, -2, -20, 10]
sum4 = -10
find_subarray_with_sum(arr4, sum4)