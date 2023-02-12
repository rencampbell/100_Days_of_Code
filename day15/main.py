from art import logo, mug_logo
from machine_menu import menu

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

money = {
    "quarters": 0,
    "dimes": 0,
    "nickles": 0,
    "pennies": 0,
}

def report(ingredients):
    return ingredients

def check_resources(ingredients,beverage):
    return ingredients

def process_coins(coins):
    return money

def make_drink(beverage):
    return beverage

drink_choice=input("What would you like? (espresso/latte/cappuccino): ").lower()
if drink_choice=="espresso" or drink_choice=="latte" or drink_choice=="cappuccino":
    report(resources)
    check_resources(resources)
    print("How many of each coin would you like to pay with?")
    for m in money:
        money[m]=float(input(f"{m}: $"))
    print(money)
    process_coins(money)
    make_drink(drink_choice)
elif drink_choice=="off":
    print("Powering Off...")
else:
    print("That was not valid input.")