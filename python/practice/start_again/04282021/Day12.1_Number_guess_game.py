# Number guess the game 
# Build a Number guessing game, in which the user selects a range.
# Let’s say User selected a range, i.e., from A to B, where A and B belong to Integer.
# Some random integer will be selected by the system and the user has to guess that integer in the minimum number of guesses
import random
import math 

EASY_LEVEL_TURN = 5
HARD_LEVEL_TUEN = 10 

def choose_answer(y,guess,moves):
    """ Check answers against guess, Returns the number if it matches """
    if y == guess :
        print (f"Guess right {guess}, range {y} ")
        return moves - 1
    elif y > guess :
        print (f"You guessed {guess} small  ")
        return moves - 1
    elif y < guess:
        print (f"You guessed {guess} big ")
        return moves - 1 
    else:
        print (f"You got it! The answer was {guess}")



def set_difficulty():
    level = input("Choose the difficulty level, 'easy' or 'hard' ")
    if level == "easy":
        return EASY_LEVEL_TURN
    else:
        return HARD_LEVEL_TUEN



def game():
    #Choose the upper and lower bounds
    lower=int(input("Enter the lower bound: "))
    upper=int(input("Enter the upper bound: "))
    #Generate a random number between upper and lower 
    y = random.randint(lower,upper)
    #print (f"Number Range would be - {y}")
    turns=set_difficulty()
    #Guess the number
    guess = 0 
    while guess != y :
        guess = int(input("Guess a number: "))
        moves = choose_answer(y, guess, turns)
        if moves == 0:
            print ("You have run out of move, you loose")
        elif guess !=y :
            print ("Guess Again !")
game()    


