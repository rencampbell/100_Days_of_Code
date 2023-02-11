import random
from art import logo

print(logo)
print("I'm thinking of a number between 1 and 100...")
answer=random.randint(1,100)
print(answer)

difficulty=input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
if difficulty=="easy":
    attempts=10
else:
    attempts=5

game_over=False

while not game_over:

    while attempts>0:
        print(f"You have {attempts} attempts remaining to guess the number.")
        guess=input("Make a guess: ")
        if guess==answer:
            print("That's right! The correct answer was {answer}. YOU WIN!")
            game_over==True
        else:
            if guess>answer:
                print("Too high.")
            else:
                print("Too low.")
            attempts-=1        