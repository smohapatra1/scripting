#   https://www.geeksforgeeks.org/python/number-guessing-game-in-python/

import random
print ("Hi!, Welcome to number guessing game. \n You have 7 chances to guess the number. Let's Start ")
low = int(input("Enter the lowest number"))
high = int(input("Enter he highest number"))
print (f"\n You have 7 chances to guess the number between {low} and {high}. Lets start")

num = random.randint(low, high)
ch = 7 
gc = 0 

while gc < ch:
    gc += 1
    guess = int(input("Enter your guess"))
    if guess == num:
        print (f"Correct! The number is {num}. You guesses it in {gc} attempts")
    elif gc >= ch and guess != num:
        print (f"Sorry! The number was {num}. Better luck next time")
    elif guess > num:
        print ("Too high!, try a lower number")
    elif guess < num:
        print ("Too low!, try a higher number")