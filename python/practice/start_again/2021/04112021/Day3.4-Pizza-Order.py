#Pizza Order
#Instructions
#Congratulations, you've got a job at Python Pizza. 
# Your first job is to build an automatic pizza order program.

#Based on a user's order, work out their final bill.

#Small Pizza: $15
#Small Pizza: $15
#Medium Pizza: $20
#Medium Pizza: $20
#Large Pizza: $25
#Large Pizza: $25
#Pepperoni for Small Pizza: +$2
#Pepperoni for Small Pizza: +$2
#Pepperoni for Medium or Large Pizza: +$3
#Pepperoni for Medium or Large Pizza: +$3
#Extra cheese for any size pizza: + $1
#Extra cheese for any size pizza: + $1

#Example Input
#size = "L"
#size = "L"
#add_pepperoni = "Y"
#add_pepperoni = "Y"
#extra_cheese = "N"
#extra_cheese = "N"

#Example Output
#Your final bill is: $28.
#Your final bill is: $28.

pizza_size=input("Enter your pizza size: ")
small_price=15
medium_price=20
large_price=25
pep_small=2
pep_large_medium=3
cheese_any=1
total=0

if pizza_size == "L":
    peporoni=input("Do you want peporoni: ")
    cheese=input("Do you want extra cheese: ")
    if peporoni == "Y" and cheese == "Y" :
        total=large_price + pep_large_medium + cheese_any
        print (f"Your final bill is: ${total}")
    elif peporoni == "Y" and cheese == "N" :
        total=large_price + pep_large_medium
        print (f"Your final bill is: ${total}")
    elif peporoni == "N" and cheese == "Y":
        total=large_price + cheese_any
        print (f"Your final bill is: ${total}")
    else:
        total=large_price
        print (f"Your final bill is: ${total}")

elif pizza_size == "M" :
    peporoni=input("Do you want peporoni: ")
    cheese=input("Do you want extra cheese: ")
    if peporoni == "Y" and cheese == "Y" :
        total=medium_price + pep_large_medium + cheese_any
        print (f"Your final bill is: ${total}")
    elif peporoni == "Y" and cheese == "N" :
        total=medium_price + pep_large_medium
        print (f"Your final bill is: ${total}")
    elif peporoni == "N" and cheese == "Y":
        total=medium_price + cheese_any
        print (f"Your final bill is: ${total}")
    else:
        total=medium_price
        print (f"Your final bill is: ${total}")
elif pizza_size == "S" :
    peporoni=input("Do you want peporoni: ")
    cheese=input("Do you want extra cheese: ")
    if peporoni == "Y" and cheese == "Y" :
        total=small_price + pep_small + cheese_any
        print (f"Your final bill is: ${total}")
    elif peporoni == "Y" and cheese == "N" :
        total=small_price + pep_small
        print (f"Your final bill is: ${total}")
    elif peporoni == "N" and cheese == "Y":
        total=small_price + cheese_any
        print (f"Your final bill is: ${total}")
    else:
        total=small_price
        print (f"Your final bill is: ${total}")
else:
    print(f"Please enter proper pizza size, you enetered {pizza_size}, it should be 'L', 'M' and 'S'")