from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
from menu import Menu, MenuItem
from art import logo, mug_logo

# List of drinks
espresso = MenuItem("espresso", 50, 0, 18, 1.5)
latte = MenuItem("latte", 200, 150, 24, 2.5)
cappuccino = MenuItem("cappuccino", 250, 100, 24, 3.0)

# For ordering drinks and checking if drink is available
menu = Menu()

# Printing report of all resources, checking if resources are sufficient, making coffee
coffee_maker = CoffeeMaker()

# Printing report and taking payment
money_machine = MoneyMachine()

making_coffee=True
print(logo)

#while making_coffee==True the while loop will continue
while making_coffee:
    #stores the type of drink the user wants
    choice=input(f"What would you like? {menu.get_items()}: ").lower()
    drink_choice=menu.find_drink(choice)
    #if choice is espresso/latte/cappuccino
    if drink_choice!= None:
        #prints the cost of the drink
         print(f"\nThat costs ${espresso.cost}")
        #reports the resources and profit left in the machine
making_coffee=False