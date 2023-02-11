from art import logo

#Blackjack House Rules

#deck is unlimited in size
#no jokers
#jack, king & queen all count as 10
#ace can count as 11 or 1
#the following list is used as the deck of cards
cards=[11,2,3,4,5,6,7,8,9,10,10,10,10]
#cards in the list have an equal probability of being drawn
#cards are not removed from the deck if they are drawn

playblackjack=True

def deal_cards():


while playblackjack:
    print(logo)
    print("Do you want to play again?\n")
    play_again=input("'Y' for yes, 'N' for no: ").upper()
    if play_again=='Y':
        playblackjack=True
    else:
        playblackjack=False