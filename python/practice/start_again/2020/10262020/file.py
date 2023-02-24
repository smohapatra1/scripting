#myfile='test.txt'
myfile=open('test.txt')
print (myfile.read())
with open('test.txt', mode='r') as new_test:
	print (new_test.read())
with open('test.txt', mode='r+') as f:
	f.write('\n I am Good, How are you')
	print (f.read())
