#Perofrm a higher and lower game 
#Generate a random number 
import random 

#Display the art 
from art import logo , vs
from game_data import data  

print ( logo)
score = 0 
is_continue = True
account_b=random.choice(data)

while is_continue:

    #Randmom account from data 
    
    account_a = account_b
    account_b=random.choice(data)
    
    if account_a == account_b:
        account_b = random.choice(data)

    #Format the account data 
    def format_data(account):
        account_name = account["name"]
        account_des = account["description"]
        account_country = account["country"]
        return f" A. {account_name} , b. {account_des} c. {account_country}"

    print (f"Compare A: {format_data(account_a)}")
    print (vs)
    print (f"Compare B: {format_data(account_b)}")

    # #Ask user for a guess
    guess = input("Enter your guess : 'A' or 'B' ").lower()
    a_follower_account=account_a["follower_count"]
    b_follower_account=account_b["follower_count"]
    print (f"A - {a_follower_account} B - {b_follower_account}")

    def check_answer (guess, a_follower_account, b_follower_account):
        if a_follower_account > b_follower_account:
            return guess == "a"
        else:
            return guess == "b"

    is_correct=check_answer(guess, a_follower_account, b_follower_account)


    #give user feedback on their guess 

    
    if is_correct:
        score +=1
        print (f"You are right - Current score {score}")
        is_continue = False
    else:
        print (f"Sorry!, you are wrong - Current score {score}")
