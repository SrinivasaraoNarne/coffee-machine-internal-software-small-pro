from menu import MENU, resources
import os


def clear():
    os.system('clear')


profit = 0


def resources_enough(order_ing):
    for item in order_ing:
        if order_ing[item] > resources[item]:
            print(f"Sorry there is not enough {item}.")
            return False
        else:
            return True


def payment_cal():
    total = 0
    total += int(input(f"how much money? $"))
    return total


def transaction(paid, drink_cost):
    if paid >= drink_cost:
        change = round(paid - drink_cost)
        if change > 0:
            print(f"Here is ${change} in change.")
        global profit
        profit += drink_cost
        return True
    else:
        return False


def make_coffee(drink_name, order_ing):
    for item in order_ing:
        resources[item] -= order_ing[item]
    print(f"Here is your {drink_name} ☕️. Enjoy!")


is_on = True

while is_on:
    print("Welcome to the coffee Machine!")
    choice = input("What would you like? (espresso/latte/cappuccino): ")
    if choice == "off":
        is_on = False
    elif choice == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${profit}")
    else:
        drink = MENU[choice]
        if resources_enough(drink["ingredients"]):
            payment = payment_cal()
            if transaction(payment, drink["cost"]):
                make_coffee(choice, drink["ingredients"])
