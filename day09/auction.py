import os
from art import logo

auction={}
go_again=True

#While the user has not typed 'no' to exit
while go_again==True:
    print(logo)
    #collects bidder name and price
    bidder_name=input("What is your name?\n")
    bidder_price=float(input("What is your price?\n$"))
    #bidder name becomes key for price entry in the auction dictionary
    auction[bidder_name]=bidder_price
    #user can indicate if there is another bidder behind them
    go=input("Type 'yes' if there is another bidder and 'no' otherwise\n").lower()
    #if there is another bidder the while loop restarts
    #the screen is also cleared so the next user cannot see the previous bid
    if go=="yes":
        go_again=True
        os.system ('cls')
    #if there is no other bidder the while loop is exited
    else:
        go_again=False

highest_bid=0
#this loop finds the highest price and stores it in var highest_bid
#also stores the name associated with that bid as highest_bidder
for member in auction:
    if auction[member]>highest_bid:
        highest_bid=auction[member]
        highest_bidder=member

#the screen is cleared and the winner announced
os.system ('cls')
print(f"The highest bid in this auction was ${highest_bid} by {highest_bidder}")
