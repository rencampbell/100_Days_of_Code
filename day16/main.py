from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
from menu import Menu, MenuItem
from art import logo, mug_logo

# List of drinks
espresso = MenuItem("espresso", 50, 0, 18, 1.5)
latte = MenuItem("latte", 200, 150, 24, 2.5)
cappuccino = MenuItem("cappuccino", 250, 100, 24, 3.0)

# For ordering drinks and checking if drink is available
menu_obj = Menu()

# Printing report of all resources, checking if resources are sufficient, making coffee
coffee_maker_obj = CoffeeMaker()

# Printing report and taking payment
money_machine_obj = MoneyMachine()

making_coffee=True

#while making_coffee==True the while loop will continue
while making_coffee:
    #prints the coffee machine logo
    print(logo)
    #stores the type of drink the user wants
    choice=input(f"What would you like? {menu_obj.get_items()}: ").lower()
    drink_choice=menu_obj.find_drink(choice)
    #if choice is espresso/latte/cappuccino
    if drink_choice!= None:
        #prints the cost of the drink
         print(f"That costs ${drink_choice.cost}")
        #reports the resources left in the machine
         coffee_maker_obj.report()
        #if not enough resources are left
         if coffee_maker_obj.is_resource_sufficient(drink_choice)==False:
            #prints error message
            print("There are not enough resources to complete your order.")
            #exits while loop
            making_coffee=False
        #if enough resources are left
         else:
            #collects payment and determines if sufficient funds were inputted
            sufficient_funds=money_machine_obj.make_payment(drink_choice.cost)
            #if sufficient funds were not deposited
            if sufficient_funds==False:
                #exits the while loop
                making_coffee=False
            #if sufficient funds were deposited
            else:
                #makes drink for the user
                coffee_maker_obj.make_coffee(espresso)
                #prints mug logo
                print(mug_logo)
                #calculates profit to be stored by machine
                money_machine_obj.report()
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