#Construct finish game with user choice 
game_choice = [0,1,2]
def game_values(game_choice):
    print ("My choices are {}".format(game_choice))
game_values(game_choice)
#Match your choices 
def choices():
    choice = "wrong"
    x=int(input("Enter your choice : "))
    while choice not in game_choice:
        if x not in game_choice:
            print ("Sorry ! {} doesn't fall uner [0,1,2,], Choose Another ".format(x))
            break
        else:
            print ("{} matches ".format(x))
            break 
choices()
def replacement(game_choice,position):
    new_value=input("Enter the new values :")
    game_choice[position] = new_value
    print ("The new values at position {} is {} and final value is {}".format(position,new_value,game_choice))
    
replacement(game_choice,1)
