#   https://www.geeksforgeeks.org/python/21-number-game-in-python/

import random

def play_21_game():
    current_number = 0 
    player_turn = 1
    print ("Welcome to 21 game! ")
    print ("Player who says '21' loose")
    while current_number < 21:
        if player_turn == 1:
            print (f"\n Current number: {current_number}")
            while True:
                try:
                    num_to_add = int(input("Your turn. Add 1,2, or 3:"))
                    if num_to_add in [1, 2, 3]:
                        break
                    else:
                        print ("Invalid input. Please enter 1, 2, or 3.")
                except ValueError:
                    print ("Invalid input. Please enter a number.")
            current_number += num_to_add
            print(f"You added {num_to_add}. Current total: {current_number}")
            if current_number >= 21:
                print("You reached 21! You lose!")
                break
            player_turn = 0
        else:
            print(f"\nCurrent number: {current_number}")
            if (current_number + 1) % 4 == 0 and current_number + 1 <= 21:
                num_to_add = 1
            elif (current_number + 2) % 4 == 0 and current_number + 2 <= 21:
                num_to_add = 2
            elif (current_number + 3) % 4 == 0 and current_number + 3 <= 21:
                num_to_add = 3
            else:
                num_to_add = random.randint(1, 3)
            if current_number + num_to_add > 21:
                num_to_add = 21 - current_number
                if num_to_add == 0: 
                    break
            print(f"Computer adds {num_to_add}.")
            current_number += num_to_add
            print(f"Current total: {current_number}")
            if current_number >= 21:
                print("Computer reached 21! Computer loses! You win!")
                break
            player_turn = 1
if __name__ == "__main__":
    play_21_game()
