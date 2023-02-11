import random
import os
from art import logo,vs
from game_data import data

game_over=False
points=0

#while the game is not over
while game_over==False: 

    #clears the screen each time the while loop restarts
    os.system ('cls')
    #displays logo from the art module
    print(logo)
    #displays the current score
    print(f"Current score: {points}")

    #chooses random dictionaries, celeb1 & celeb2 from the data list
    celeb1=random.choice(data)
    celeb2=random.choice(data)
    #displays name, description and country of each celeb
    print(f"Compare A: {celeb1['name']}, a {celeb1['description']}, from {celeb1['country']}")
    print(vs)
    print(f"Against B: {celeb2['name']}, a {celeb2['description']}, from {celeb2['country']}")
    #prompts the user to guess who has more followers
    guess=input("Who has more followers? Type 'A' or'B': ").upper()
    
    #if the user guesses A correctly their points increase by 1
    if guess=='A' and celeb1['follower_count']>celeb2['follower_count']:
        points+=1
    #if the user guesses B correctly their points increase by 1
    elif guess=='B' and celeb1['follower_count']<celeb2['follower_count']:
        points+=1
    #otherwise the game is ended and final score showm
    else:
        print(f"You're wrong. Final score: {points}")
        print("Game over.")
        game_over=True