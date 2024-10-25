from ascii_art import logo

from os import system, name


def clear() -> None:
    """
    Clear console
    """
    # for windows
    if name == "nt":
        _ = system("cls")
    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system("clear")


def check_highest(bidders: dict) -> None:
    """
    To check the highest bidder
    :param bidders:
    """
    highest: int = 0
    winner: str = ""

    for bidder in bidders:
        bid_price = bidders[bidder]
        if bid_price > highest:
            highest = bid_price
            winner = bidder

    print(f"The winner is {winner} with a bid of ${highest}")


auctioneers: dict[str, int] = {}

print(logo)
print("Welcome to the secret auction program.")

bidding_finished: bool = False

while not bidding_finished:
    bidder_name: str = input("What is You name? ")
    price: int = int(input("What's Your bid? $"))
    auctioneers[bidder_name] = price
    should_continue: str = input("Are there any other bidders? Type 'yes' or 'no'\n")
    if should_continue == "no":
        bidding_finished = True
        clear()
        check_highest(auctioneers)
    elif should_continue == "yes":
        clear()
    else:
        should_continue: str = input("Please type 'yes' or 'no'\n")
        clear()
