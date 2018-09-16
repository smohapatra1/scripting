#!/bin/sh
#Enter your name
#If you name matches, print name
#Else print incorrect name
echo  "Enter your name : "
read name
if [[ $name = "samar" ]] ; then
   echo "My name is $name"
else
   echo "Incorect name"
fi
