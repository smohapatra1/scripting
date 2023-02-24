#Treaure island
# Condictional stuff 
print("Welcome to Treasure Island : ")
choice=input("Enter your move: ")
turn=choice.lower()
if choice == "right":
    print ("Fall into a hole, Game Over")
elif choice == "left":
    task=input("Enter - swim or wait: ")
    task1=task.lower()
    if task1 == "swim":
        print ("Attacked by Tout, Game Over")
    elif task1 == "wait":
        door=input("Which Door ? : ")
        color=door.lower()
        if color == "red":
            print ("Burnd by Fire, Game Over")
        elif color == "blue" :
            print ("Eaten by beast, Game Over")
        elif color == "yellow":
            print ("You Win")
        else:
            print ("Game Over")
    else:
        print ("Attacked by Tout, Game Over")

else:
    print ("Fall into a hole, Game Over")