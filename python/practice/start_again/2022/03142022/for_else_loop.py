#For else loop
# Print numbers from 2 to 10, if number is 7, Exit the loop
for i in range(2,10):
    print (i)
    if i % 17 == 0 :
        break
        print ("Exit the loop")
else:
    print("After the loop")