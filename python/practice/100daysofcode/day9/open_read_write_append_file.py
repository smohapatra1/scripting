#!/usr/bin/python
#Open Read and Write a file
#Write
def main():
    f=open("test.txt", "wa+")
    for i in range(10):
        f.write("Line %d \n" % (i+1))
#Append
    for i in range(2):
        f.write("Appened line %d\n" %(i+1))
#Read        
    f=open("test.txt", "r")
    if f.mode == "r":
        files=f.read()
        print (files)        
#ReadLines
    f=open("test.txt", "r")
    x = f.readlines()
    i = 0
    for x1 in x:
        print ("Reading line %d - %s" % (i+1, x1) )
        i = i + 1

if __name__ == "__main__":
    main()
