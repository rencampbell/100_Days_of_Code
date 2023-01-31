#allows the user to play rock, paper, scissors against a computer
#each element is assigned a value, from 0 to 2

#imports 'random' module
import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#player is prompted to input a value which represents rock, paper or scissors
player_choice=int(input("What do you choose? Type 0 for ROCK, 1 for PAPER or 2 for SCISSORS: "))

if player_choice==0:
    print(rock)
elif player_choice==1:
    print(paper)
else:
    print(scissors)

#computer generates a random integer, between 0 & 2, which represents rock, paper or scissors
computer_choice=random.randint(0,2)

#the computer's 'choice' is outputted to the user
print("Computer chose: ")

if computer_choice==0:
    print(rock)
elif computer_choice==1:
    print(paper)
else:
    print(scissors)

#overall verdict is printd
if player_choice==0 and computer_choice==2:
    print("You win!")
elif player_choice==1 and computer_choice==0:
    print("You win!")
elif player_choice==2 and computer_choice==1:
    print("You win!")
elif player_choice==computer_choice:
    print("Draw!")
else:
    print("You lose!")



