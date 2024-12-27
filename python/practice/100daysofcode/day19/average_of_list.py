#!/usr/bin/python
#Complete the following program such that it calculates and prints the average of the elements of the given list.
sample_list = [ 2, 10, 3, 5]
#for i in sample_list:
llist=len(sample_list)
print ("No of lits %s" %llist)
total= sample_list[0] + sample_list[1] + sample_list[2] + sample_list[3]
avg=float(total/llist)
print ("Avg %s" % avg)

