from art import logo, mug_logo
from machine_menu import MENU

print(logo)

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

cache=0.0

def report(ingredients,coins):
    print("\nReport:")
    for item in ingredients:
        print(f"{item}: {ingredients[item]}ml")
    print(f"money: ${round(cache,2)}")
    

def check_resources(beverage):
    resources['water']-=MENU[beverage]['ingredients']['water']
    resources['milk']-=MENU[beverage]['ingredients']['milk']
    resources['coffee']-=MENU[beverage]['ingredients']['coffee']
    if resources['water']<0 or resources['milk']<0 or resources['coffee']<0:
        enough_resources=False
    else:
        enough_resources=True
    return enough_resources

def convert(coins):
    total=coins["quarters"]*0.25+coins["dimes"]*0.1+coins["nickles"]*0.05+coins["pennies"]*0.01
    return total

def process_coins(coins):
    total=convert(coins)
    print(f"\nYou paid: ${round(total,2)}")
    if total>MENU[drink_choice]['cost']:
        enough_money=True
        change=total-MENU[drink_choice]['cost']
        print(f"Your change is: ${round(change,2)}")
    elif total==MENU[drink_choice]['cost']:
        enough_money=True
        print(f"You paid just enough. No change.")
    else:
        enough_money=False
        print("You did not deposit sufficient funds.")
    return enough_money

def make_drink(beverage):
    print(f"\nHere's your {beverage}: ")
    print(mug_logo)

making_coffee=True

while making_coffee:
    drink_choice=input("What would you like? (espresso/latte/cappuccino): ").lower()
    if drink_choice=="espresso" or drink_choice=="latte" or drink_choice=="cappuccino":
        print(f"\nThat costs ${MENU[drink_choice]['cost']}")
        report(resources,money)
        if check_resources(drink_choice)==False:
            print("There are not enough resources to complete your order.")
            making_coffee=False
        else:
            print("\nOrder coming up!")
            print("\nHow many of each coin would you like to pay with?")
            for m in money:
                money[m]=float(input(f"{m}: "))
            sufficient_funds=process_coins(money)
            if sufficient_funds==False:
                making_coffee=False
            else:
                make_drink(drink_choice)
    elif drink_choice=="off":
        print("Powering Off...")
    else:
        print("That was not valid input.")