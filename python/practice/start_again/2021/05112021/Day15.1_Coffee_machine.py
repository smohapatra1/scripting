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
profit = 0 
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

#Resouce sufficent 
def is_resource_sufficent(order_ingredients):
    for item in order_ingredients:
        if order_ingredients[item] >= resources[item]:
            print (f"Sorry there is not enough {item}")
            return False
        return True

# Process coins 
def process_coins():
    """ Retuns the total calculated from coins entered """
    print ("Please insert coins: ")
    total = int(input("How many quarters? : ")) * .25
    total += int(input("How many dimes? : ")) * .1
    total += int(input("How many nickles? : ")) * .05
    total += int(input("How many penniess? : ")) * .01
    return total

def is_transcation_successful(money_received, drink_cost):
    """ Return True when the payments is accepted  or False when payment is insufficent """
    if money_received >= drink_cost:
        change = round(money_received - drink_cost)
        print (f"Here is your change ${change}")
        global profit 
        profit += drink_cost 
        return True
    else:
        print ("Sorry there is not enough money, Money Returned")
        return False

#7. Make coffee
def make_coffee (drink_name, order_ingredients):
    """ Deduct the required ingredients from the resources """
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print (f"Here is your drink {drink_name}")

#1: prompt user by asking "What would you like? (Expresso /Latte/cappucino):"
is_on = True
while is_on:
    choice = input("What would you like? (espresso/latte/cappuccino?) ").lower()
    if choice == "off":
        is_on=False
#Choice Resource         
    elif choice == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${profit}")
#Enough Resources
    else:
        drink = MENU[choice]
        print (drink)
        if is_resource_sufficent(drink["ingredients"]):
            payment = process_coins()
            if is_transcation_successful(payment, drink["cost"]):
                make_coffee(choice, drink["ingredients"])



