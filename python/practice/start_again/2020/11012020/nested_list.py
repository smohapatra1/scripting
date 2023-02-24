#Reassign 'hello' in this nested list to say 'goodbye' instead:
a = [1, 2, "hello",[1,2,"goodbye"]]
print ("First print GoodBye :  {}".format(a[3][2]))
#a= a[3][2]
print ("Replacing goodbye with hello : {}".format(a[:]))
print ("3rd place value {}".format(a[2]))

