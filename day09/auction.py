import os
from art import logo

auction={}
go_again=True

while go_again==True:
    print(logo)
    bidder_name=input("What is your name?\n")
    bidder_bid=float(input("What is your price?\n$"))
    auction[bidder_name]=bidder_bid
    go=input("Type 'yes' if there is another bidder and 'no' otherwise\n").lower()
    if go=="yes":
        go_again=True
        os.system ('cls')
    else:
        go_again=False

highest_bid=0
for member in auction:
    if auction[member]>highest_bid:
        highest_bid=auction[member]
        highest_bidder=member

os.system ('cls')
print(f"The highest bid in this auction was ${highest_bid} by {highest_bidder}")
