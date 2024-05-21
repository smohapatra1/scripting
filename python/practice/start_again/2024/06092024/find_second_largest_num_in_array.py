#   How would you find the second largest number in an array?

def Largest2nd(arr, n ):
    arr.sort(reverse = True)
    for i in range(n):
        if arr[i] != arr[0]:
            return arr[i] 
    return
if __name__ == "__main__":
    arr = [12, 35, 100, 10, 99, 1]
    
    n = len(arr)
    result = Largest2nd(arr, n)
    print (result)