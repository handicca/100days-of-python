import art
from os import system, name


def clear():
    # for Windows
    if name == "nt":
        _ = system("cls")
    # for Mac and Linux(here, os.name is 'posix')
    else:
        _ = system("clear")


def check_highest(bidders):
    highest = 0
    winner = ""
    for bidder in bidders:
        bid_price = bidders[bidder]
        if bid_price > highest:
            highest = bid_price
            winner = bidder
    print(f"The winner is {winner} with a bid of ${highest}")


auctioneers = {}
print(art.logo)
print("Welcome to the secret auction program.")

end = False
while not end:
    bidder_name = input("What is you name? ")
    price = int(input("What's your bid: $"))
    auctioneers[bidder_name] = price
    next_bidder = input("Are there any other bidders? Type 'yes' or 'no'\n").lower()
    if next_bidder == "no":
        end = True
        clear()
        check_highest(auctioneers)
    elif next_bidder == "yes":
        clear()
    else:
        next_bidder = input("Please type 'yes' or 'no'\n")
        clear()
