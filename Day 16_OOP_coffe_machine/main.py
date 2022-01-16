from random import choice
from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
machine = CoffeeMaker()
money = MoneyMachine()
machine_working = True
while machine_working:
    choice = input(f"What would you like? ({menu.get_items()}): ").lower()
    if choice == 'off':
        machine_working = False
    elif choice == 'report':
        machine.report()
        money.report()
    else:
        drink = menu.find_drink(choice)
        if drink != None and machine.is_resource_sufficient(drink) and money.make_payment(drink.cost):
            machine.make_coffee(drink)
