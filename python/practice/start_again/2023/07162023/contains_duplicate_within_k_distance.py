#Check if a given array contains duplicate elements within k distance from each other

def containsDuplicate(arr, n, k ):
    myset=[]
    for i in range(n) :
        if arr[i] in myset:
            return True
        myset.append(arr[i])
        if (i>=k):
            myset.remove(arr[i - k])
    return False 
if __name__ == "__main__":
    arr=[10, 5, 3, 1, 4, 2, 6]
    n=len(arr)
    if (containsDuplicate( arr, n, 3)):
        print ("Duplicate Exists")
    else:
        print ("Duplicate doesn't exist")
