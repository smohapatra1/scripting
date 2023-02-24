#Write a virtual coin toss programm. It will randomly tell the user Heads or Tails
import random
print (" Welcome to coin toss: ")
toss=random.randint(0,1)
if toss == 1:
    print ("Heads")
else:
    print ("Tails")