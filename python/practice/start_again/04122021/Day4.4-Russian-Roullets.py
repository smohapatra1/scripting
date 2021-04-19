#Who's Paying
#Instructions
#You are going to write a program which will select a random name from a list of names. 
# The person selected will have to pay for everybody's food bill.

#Important: You are not allowed to use the choice() function.

#Don't worry about the lines 3/4 it's there to allow us to test your code.

#Line 8 splits the string namesAsCSV into individual names and puts them inside a List called names.

#Example Input
#Angela, Ben, Jenny, Michael, Chloe

#Example Output
#Michael is going to buy the meal today!

#e.g. When you hit run, this is what should happen:
import random
name=input("Enter your names in comma separated: ")
#Split into numbers 
names=name.split(",")
num_items=len(names)
pick_name=random.randint(0, num_items - 1)
person=names[pick_name]
#Length of the numbers 
print (f"{person}, is going to by the meals - Not choice Module ")
#Choice module 
print (f"{random.choice(names)} is going to pay the bill- Choice module ")