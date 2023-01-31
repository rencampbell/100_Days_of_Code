#password generator
#outputs a random password based on the number of letters, symbols and numbers chosen by the user

#imports 'random' module
import random

#stores possible letters, numbers & symbols in lists
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

#asks the user to choose number of letters, numbers & symbols
print("Welcome to the PyPassword Generator!")
nr_letters= (input("How many letters would you like in your password?\n"))
nr_symbols = (input(f"How many symbols would you like?\n"))
nr_numbers = (input(f"How many numbers would you like?\n"))

#defines password as a str
password=""

#adds a random member from the list of letters to password each time the loop is executed
for letter in range(1, int(nr_letters)+1):
    i=random.randint(0,25)
    password=letters[i]+password

#adds a random member from the list of symbols to password each time the loop is executed
for symbol in range(1, int(nr_symbols)+1):
    i=random.randint(0,8)
    password=symbols[i]+password

#adds a random member from the list of numbers to password each time the loop is executed
for number in range(1, int(nr_numbers)+1):
    i=random.randint(0,9)
    password=numbers[i]+password

#cosverts the str var, password into a list then shuffles list
password=list(password)
random.shuffle(password)

#outputs final password by converting shuffled list back into a string
print("Your password is: ")
print(''.join(password))
