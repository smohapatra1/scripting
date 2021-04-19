# Ask 0 for Rock, 1 for Paper or 2 for Scissors
#Play against the compute and to show You Won or You Loose 
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
#print (rock)
#print (paper)
#print (scissors)

import random
game_images=[rock,paper,scissors]
you_choose=int(input("Enter your choice: "))
computer=random.randint(0,2)
print (f"Computer choose - {computer}")
if you_choose >=3 or you_choose < 0:
    print ("You types an invalid number")
    print (game_images[you_choose])
else:
    print (game_images[computer])
    if you_choose == 0 and computer == 2:
        print ("You Win")
    elif computer == 0 and you_choose == 2:
        print ("You Losse")
    elif computer > you_choose :
        print ("You loose")
    elif you_choose > computer:
        print ("You Win")
    elif computer == you_choose:
        print ("It's a draw")
    else:
        print ("You Types and invalid number ")