from art import logo
import random
import os


#the following list is used as the deck of cards
cards=[11,2,3,4,5,6,7,8,9,10,10,10,10]

#deals two random numbers to user from the cards list
def deal_initial_cards (hand):
    n1=random.randint(0,12)
    hand.append(n1)
    n2=random.randint(0,12)
    hand.append(n2)

#adds a card from the cards list to whatever hand is passed as a parameter
def add_card (hand):
    hand.append(cards[random.randint(0,12)])

#calculates and returns the score of the hand passed as a parameter
def calculate_score (hand):
    score=0
    for card in hand:
        score+=card
    return score

#checks if an ace(11) is present in the player's hand
#according to the rules of blackjack, if the player's hand goes over 21 the ace can take the value 1, instead of 11
#this function also prints a statement alerting the user to the change
def check_for_ace (player,hand):
    score=calculate_score(hand)
    if score>21:
        for i in range(len(hand)):
            if hand[i]==11:
                hand[i]=1
                print(f"{player} had an ace!")
                print(f"{player}'s NEW hand: {hand}, score: {calculate_score(hand)}")

#prints the cards the user currently posesses, as well as their score
#this function calls check_for_ace() so that if the users total is over 21 the ace is replaced
def print_stats (player,hand):
    print(f"{player}'s hand: {hand}, score: {calculate_score(hand)}")
    check_for_ace (player,hand)
    
#determines who won the game, taking all rules into consideration
#the function then prints an appropriate message
def determine_winner(player, player_hand, computer_hand):
    player_score=calculate_score(player_hand)
    computer_score=calculate_score(computer_hand)
    if player_score>21:
         print("You went over. You lose.")
    elif player_score==21:
         print("BLACKJACK! You win.")
    elif player_score<21 and player_score>computer_score:
        print("Your score was higher. You win.")
    elif player_score==computer_score:
         print("Tie. Nobody wins.")
    else:
        print("Your score was lower. You lose.")

#it is initially assumed that the user wishes to play blackjack  
playblackjack=True

#while the user indicates they wish to play blackjack this loop will repeat
while playblackjack:

    #prints logo from the art module
    print(logo)

    #initializes the variables computer_cards and user_cards as empty lists
    computer_cards=[]
    user_cards=[]
    #stores the user's name
    username=input("Enter your username: ")
    print("\n")

    #calls upon the deal_initial_cards() function which gives the user their 1st two cards
    deal_initial_cards(user_cards)
    #prints the user's cards and score
    print_stats(username,user_cards)

    #gives the computer its 1st card
    add_card(computer_cards)
    #prints the computer's card and score
    print_stats('Computer',computer_cards)
    print("\n")

    #finds out if the user would like to add more cards to their hand
    more_cards=input("Type 'Y' to get another card, 'N' to pass: ").upper()
    if more_cards=='Y':
        add_card(user_cards)

    #gives the computer its final card
    add_card(computer_cards)

    #prints the final cards and score for the user and the computer
    print("\nFinal standing:\n")
    print_stats(username,user_cards)
    print_stats('Computer',computer_cards)
    print("\n")

    #determines who won the game, taking all rules into consideration
    determine_winner(username, user_cards, computer_cards)

    #if the user wants to play again the screen is cleared and while loop is repeated (game starts again)
    #otherwise, the while loop is exited
    print("Do you want to play again?\n")
    play_again=input("'Y' for yes, 'N' for no: ").upper()
    if play_again=='Y':
        playblackjack=True
        os.system ('cls')
    else:
        playblackjack=False