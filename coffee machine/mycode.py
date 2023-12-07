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
    "Money": 0
}


def resource_check(drink):
    """resources are checked"""
    if resources["water"] < MENU[drink]["ingredients"]["water"]:
        print("Sorry there is not enough water.")
        return False
    elif resources["coffee"] < MENU[drink]["ingredients"]["coffee"]:
        print("Sorry there is not enough coffee.")
        return False
    if drink == "latte" or drink == "cappuccino":
        if resources["milk"] < MENU[drink]["ingredients"]['milk']:
            print("Sorry there is not enough Milk.")
            return False
        else:
            resources["water"] -= MENU[drink]["ingredients"]["water"]
            resources["coffee"] -= MENU[drink]["ingredients"]["coffee"]
            resources["milk"] -= MENU[drink]["ingredients"]["milk"]
            return True
    else:
        resources["water"] -= MENU[drink]["ingredients"]["water"]
        resources["coffee"] -= MENU[drink]["ingredients"]["coffee"]
        return True


def take_money(drink):
    """prints the change of take money or print not enough money is inserted"""
    print("Please inert coins.")
    quarters = int(input("how many quarters?: ")) * 0.25
    dimes = int(input("how many dimes?: ")) * 0.10
    nickles = int(input("how many nickles?: ")) * 0.05
    pennies = int(input("how many pennies?: ")) * 0.01

    total_money = quarters + dimes + nickles + pennies

    if total_money < MENU[drink]["cost"]:
        print("Sorry that's not enough money. Money refunded.")
        return False
    else:
        change = total_money - MENU[drink]["cost"]
        resources["Money"] += MENU[drink]["cost"]
        print(f"Here is ${round(change, 2)} in change")
        return True


def machine():
    order = input("“What would you like? (espresso/latte/cappuccino): ").lower()
    if order == "report":
        print(f"Water: {resources["water"]} \nMilk: {resources["milk"]} \nCoffee: {resources["coffee"]}")
        print(f"Money: ${resources["Money"]}")
    elif order == "off":
        return
    elif resource_check(order):
        if take_money(order):
            print(f"Here is your {order} ☕️. Enjoy!")
    machine()


machine()