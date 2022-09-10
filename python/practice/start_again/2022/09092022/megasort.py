#megasort

def megasort(arr):
    n=len(arr)
    if n > 1:
        mid=n//2
        L=arr[:mid]
        R=arr[mid:]
        
        megasort(L)
        megasort(R)
        i=j=k=0
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i+=1
            else:
                arr[k] = R[j]
                j+=1
            k+=1
        while i < len(L):
            arr[k] = L[i]
            i+=1
            k+=1
        while j < len(R):
            arr[k] = R[j]
            j+=1
            k+=1
def printmega(arr):
    for i in range(len(arr)):
        print (arr[i], end=" ")
    print()



if __name__ == '__main__':
    arr=[1,2, 7, 8, 10, 11]
    megasort(arr)
    printmega(arr)
