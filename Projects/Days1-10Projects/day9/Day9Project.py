# day9 secret auction program

from replit import clear
from art import logo

print(logo)
bids = {}
biddingFinished = False


def findHighestBidder(biddingRecord):
    highestBid = 0
    for bidder in biddingRecord:
        bidAmount = biddingRecord[bidder]
        if bidAmount > highestBid:
            highestBid = bidAmount
            winner = bidder
    print(f"The winner is {winner} with a bid of ${highestBid}")


while not biddingFinished:
    name = input("what is your name ?\n")  # key
    price = int(input("what is your bid?: $\n"))  # value
    bids[name] = price
    shouldContiune = input("are there any bidders? type 'yes' or 'no' \n")
    if shouldContiune == "no":
        biddingFinished = True
        findHighestBidder(bids)
    elif shouldContiune == "yes":
        clear()
