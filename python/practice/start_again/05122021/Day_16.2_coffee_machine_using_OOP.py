from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

money_machine = MoneyMachine()
cofee_maker = CoffeeMaker()
menu = Menu()
cofee_maker.report()
money_machine.report()


is_on = True
while is_on:
    options = menu.get_items()
    choice=input(f"What would you like? ({options}):")
    if choice == "off":
        is_on=False
    elif choice == "report":
        money_machine.report()
        cofee_maker.report()
    else:
        drink = menu.find_drink(choice)
        if cofee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
            cofee_maker.make_coffee(drink)
            


        




