import time
import timeit
#Start Time
start_time = time.time()

#Script1
def fun_one(n):
    print ([str(num) for num in range(n)])
#        print (num)
fun_one(10)
#Function 2
def fun_two(n):
    print (list(map(str,range(n))))
fun_two(20)
#End Time
end_time= time.time()
elapsed_time = end_time - start_time
print (elapsed_time)
