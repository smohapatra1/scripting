#   https://www.geeksforgeeks.org/python/python-program-for-word-guessing-game/

import random

name = input("What is your name ?")
print ("Good Luck !", name)
words = ['rainbow', 'computer', 'science', 'programming', 'python', 'services', 'water' , 'liquid', 'gas']
word = random.choice(words)

print ("Guess the word : ")
guesses = ''
turns = 12 
while turns > 0:
    failed = 0 
    for char in word:
        if char is guesses:
            print (char, end=" ")
        else:
            print ("_")
            failed +=1
    if failed == 0:
        print ("You Win!")
        print ("The word is : ", word)
        break
    print ()
    guess = input("Guess a character: ")
    guesses += guess
    if guess not in word:
        turns -= 1
        print ("Wrong")
        print ("You have", + turns , 'more guesses')
        if turns == 0:
            print ("You loose")