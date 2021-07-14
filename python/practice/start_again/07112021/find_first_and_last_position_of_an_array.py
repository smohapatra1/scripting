#Find the first and last position of an sorted array
#Sorted Array - > Use bianry search 

def FirstLastPosition(nums,target):
    first = -1
    last = -1
    n= len(nums)
    for i in range(0,n):
        if target != nums[i]:
            continue
        if (first == -1):
            first = i 
        last =i
    if first != -1:
        print (f'Fist Occurance of {target} = {first}',
        f'\nLast Occurance of {target} = {last}')
    else:
        print (f'{target} Not Found')

nums = [1,5,7,7,8,8,1]
target = 1
result= FirstLastPosition(nums,target)

