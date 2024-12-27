#!/usr/bin/python
#Write a Python program to accept a filename from the user and print the extension of that
filename = raw_input("Input the Filename: ")
if "." not in filename:
    print ("Plese entrer correct extention of the file")
else:
    extn=filename.split(".")
    print ("The extension of the file is : %s " %  extn[1])
