#Write a function to post the honnred worker
work_hours=[('Ram', 10000), ('Gan', 20000), ('pan', 300) ]
current_max = 0 
emp = ''
for name,hour in work_hours:
	#print ("{} -> {}".format(current_max,hour))
	if hour > current_max:
		current_max = hour
		#print (current_max)
		emp = name
		#print (emp)
		print ("{} : {}".format(emp,current_max))
	else:
		pass

#Using Fcunction
def work(work_hours):
	current_max = 0 
	emp_of_the_month = ''
	for emp, hour in work_hours:
		#print (emp)
		if hour > current_max:
			current_max = hour
			#print (current_max)
			emp_of_the_month = emp
			#print (emp_of_the_month)
		else:
			pass
	return (emp_of_the_month, current_max)
result = work(work_hours)
print (result)
