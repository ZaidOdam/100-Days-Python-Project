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
money = 0


def check_resources(menu):
    global resources
    for i in menu:
        if resources[i] < menu[i]:
            print(f'Sorry there is not enough {i}.')
            return False
    return True


def make_drink(drink):
    global resources
    for i in drink:
        resources[i] -= drink[i]


def make_transaction(cost):
    global money
    #  quarters = $0.25, dimes = $0.10, nickles = $0.05, pennies = $0.01
    temp = {'quarters': 0, 'dimes': 0, 'nickle': 0, 'pennies': 0}
    print("Please insert coin.")
    for i in temp:
        temp[i] = int(input(f"How many {i}?: "))

    total = temp["quarters"]*0.25+temp["dimes"] * 0.10 + \
        temp["nickle"]*0.05+temp["pennies"]*0.01
    if total < cost:
        print("Sorry that's not enough money. Money refunded.")
        return False

    if total > cost:
        change = round(total-cost, 2)
        print(f'Here is {change} dollars in change.')
    money += cost
    return True


machine_state = True
while machine_state:
    choice = input(
        "What would you like? (espresso/latte/cappuccino): ").lower()
    if choice == 'off':
        machine_state = False
    elif choice == 'report':
        print(
            f"Water: {resources['water']}ml\nMilk: {resources['milk']}ml\nCoffee: {resources['coffee']}g\nMoney: ${money}")
    else:
        drink = MENU[choice]
        if check_resources(drink['ingredients']) and make_transaction(drink["cost"]):
            make_drink(drink['ingredients'])
            print(f"Here is your {choice} ☕. Enjoy!")
