import random
from art import logo

#prints logo from the art module
print(logo)
print("I'm thinking of a number between 1 and 100...")
#generates answer as random number between 1 and 100
answer=random.randint(1,100)

#allows the user to choose their level of difficulty
difficulty=input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
#if the user gets 10 chances if they select easy and 5 chances if they select hard
if difficulty=="easy":
    attempts=10
else:
    attempts=5

#while the user has not exhausted their attempts
while attempts>0:
    #prints the number of attempts remaining
    print(f"\nYou have {attempts} attempts remaining to guess the number.")
    #allows the user to guess what the answer is
    guess=int(input("Make a guess: "))
    #if they guess correctly a congratulatory message appears and the game is ended
    if guess==answer:
        print(f"That's right! The correct answer was {answer}. YOU WIN!")
        attempts=0
    #if they guess incorrectly they are given a hint
    else:
        if guess>answer:
            print("Too high.")
        else:
            print("Too low.")
        #if they guess incorrectly an attempt is subtracted
        attempts-=1
        #if attempts=0 a message states that the user lost
        if attempts==0:
            print(f"\nThe correct answer was {answer}. YOU LOSE!")
