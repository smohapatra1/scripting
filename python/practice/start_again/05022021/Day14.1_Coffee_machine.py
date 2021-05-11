MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

# 1. Print receipt 
# 2. Check resource sufficent 
# 3. Coin based only 
        # should refund if my money is not much 
        # Coin - Return if I inserted more 

# 4. Check transcaction successful 
# 5. Make cofee 



#1: prompt user by asking "What would you like? (Expresso /Latte/cappucino):"
need=input("What would you like? (Expresso(exp)/Latte(latte)/Cappucino(cappu)?) ")
def ask_user ():
    
    if need == "exp":
        print ("Go to make the expresso:")
        ask_report=input("Please enter 'r' for report: ")
        if ask_report == "r":
            report(w="water",m="milk",c="cofee",d="money")
        else:
            print (f"Experienced worker :) ")
    elif need == "latte":
        print ("Go to make the Latte:")
        ask_report=input("Please enter 'r' for report: ")
        if ask_report == "r":
            report(w="water",m="milk",c="cofee",d="money")
        else:
            print (f"Experienced worker :) ")
    elif need == "cappu":
        print ("Go to make the cappu:")
        ask_report=input("Please enter 'r' for report: ")
        if ask_report == "r":
            report(w="water",m="milk",c="cofee",d="money")
        else:
            print (f"Experienced worker :) ")
def report(w="water",m="milk",c="cofee",d="money"):
    w = "100"
    m = "50"
    c = "76"
    d = "2.5"
    print (f"Your cofee {need} is ready and your amount is : ${d}")


ask_user()
#report(w="water",m="milk",c="cofee",d="money")