#!/usr/bin/python
#Write a program which prints the sum of numbers from 1 to 101 that are divisible by 5. ( 1 and 101 are included) (Use while loop)
st = []
num = 0
count = 0
while num <= 101 :
    num +=1
    #print num
    if num % 5 == 0:
        st.append(str(num))
        print ("The numbers are %d" % num)
        count = count + num
     
print ("Total = %d " % count)
#Store in an array
nums = [','.join(st)]
print ("Nums in Array : %s" % nums)

