#Adding even numbers using for loop

even=input("Enter numbers with space: ").split()
total=0
for nums in even:
    #print (nums)
    if int(nums) % 2 == 0:
        total = total + int(nums)
print (f"Sum of even numbers: {total}")
