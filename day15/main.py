from art import logo, mug_logo
from machine_menu import MENU

#prints coffee machine logo
print(logo)

#stores the level of each resource left in the coffee machine
#after each order this dictionary is updated to show new levels
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

#stores the money paid by the customer
money = {
    "quarters": 0,
    "dimes": 0,
    "nickles": 0,
    "pennies": 0,
}

#stores the profit made by the machine
profit=0.0

#reports the level of each ingredient as well as the profit in the machine
def report(ingredients,cache):
    print("\nReport:")
    #for each item in the ingredients dictionary
    for item in ingredients:
        #prints the key as well as the level of each ingredient
        print(f"{item}: {ingredients[item]}ml")
    #prints the value of cache, rounded to two decimal places
    print(f"money: ${round(cache,2)}")
    
#checks that the resources in the machine are sufficient to complete each order
def check_resources(beverage):
    #subtracts resources needed to makke beverage from resources left in machine
    resources['water']-=MENU[beverage]['ingredients']['water']
    resources['milk']-=MENU[beverage]['ingredients']['milk']
    resources['coffee']-=MENU[beverage]['ingredients']['coffee']
    #if the remainder is less than 0 then there are not sufficient resources to make the order
    if resources['water']<0 or resources['milk']<0 or resources['coffee']<0:
        enough_resources=False
    else:
        enough_resources=True
    return enough_resources

#converts coins from quarters, dimes, nickles and pennies into a total dollars and cents value
def convert(coins):
    total=coins["quarters"]*0.25+coins["dimes"]*0.1+coins["nickles"]*0.05+coins["pennies"]*0.01
    return total

#determines if the user deposited sufficient funds and calculates their change
def process_coins(coins):
    total=convert(coins)
    #prints the total money deposited, rounded to two decimal places
    print(f"\nYou paid: ${round(total,2)}")
    #if the money deposited is greater than the cost of the drink
    if total>MENU[drink_choice]['cost']:
        #sufficient funds were deposited
        enough_money=True
        #calculates the change to be returned
        change=total-MENU[drink_choice]['cost']
        #prints the change, rounded to two decimal places
        print(f"Your change is: ${round(change,2)}")
    #if the money deposited is equal to the cost of the drink
    elif total==MENU[drink_choice]['cost']:
        #sufficient funds were deposited
        enough_money=True
        #prints that no change left
        print(f"You paid just enough. No change.")
    else:
        #sufficient funds were NOT deposited
        enough_money=False
        #prints error message
        print("You did not deposit sufficient funds.")
    #return if sufficient funds were deposited (true or false)
    return enough_money

#calculates the profit to be stored in the machine after each transaction
def calculate_profit (coins, cache):
    total=convert(coins)
    #the profit is equal to the total minus the change
    cache+=total-(total-MENU[drink_choice]['cost'])
    return cache

#makes the drink for the customer
def make_drink(beverage):
    print(f"\nHere's your {beverage}: ")
    print(mug_logo)

making_coffee=True

#while making_coffee==True the while loop will continue
while making_coffee:
    #stores the type of drink the user wants
    drink_choice=input("What would you like? (espresso/latte/cappuccino): ").lower()
    #if choice is espresso/latte/cappuccino
    if drink_choice=="espresso" or drink_choice=="latte" or drink_choice=="cappuccino":
        #prints the cost of the drink
        print(f"\nThat costs ${MENU[drink_choice]['cost']}")
        #reports the resources and profit left in the machine
        report(resources,profit)
        #if not enough resources are left
        if check_resources(drink_choice)==False:
            #prints error message
            print("There are not enough resources to complete your order.")
            #exits while loop
            making_coffee=False
        #if enough resources are left
        else:
            print("\nOrder coming up!")
            print("\nHow many of each coin would you like to pay with?")
            #for each key in the money dictionary (quarters, dimes, nickles and pennies)
            for m in money:
                #replaces each entry with a float, inputted by the user
                money[m]=float(input(f"{m}: "))
            #determines if sufficient funds were inputted
            sufficient_funds=process_coins(money)
            #if sufficiend funds were not deposited
            if sufficient_funds==False:
                #exits the while loop
                making_coffee=False
            #if sufficiend funds were deposited
            else:
                #makes drink for the user
                make_drink(drink_choice)
                #calculates profit to be stored by machine
                profit=calculate_profit(money,profit)
    #if choice is off, powers down the machine
    elif drink_choice=="off":
        print("Powering Off...")
        #exits the while loop
        making_coffee=False
    #if choice is none of the valid options
    else:
        #prints an error message
        print("That was not valid input.")
        #exits the while loop
        making_coffee=False