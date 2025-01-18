import random
from art import logo, vs
from game_data import data
from os import system, name


def clear():
    # for Windows
    if name == "nt":
        _ = system("cls")
    # for Mac and Linux(here, os.name is 'posix')
    else:
        _ = system("clear")


def format_data(account):
    """Takes the account data an returns the printable format."""
    name = account["name"]
    description = account["description"]
    country = account["country"]
    return f"{name}, a {description}, from {country}"


def check_answer(guess, a_followers, b_followers):
    """Takes the user guess and follower count and returns if they got it right."""
    if a_followers > b_followers:
        return guess == "a"
    else:
        return guess == "b"


# Display art
print(logo)

score = 0
account_b = random.choice(data)
end = False

# Make the game repeatable.
while not end:
    # Generate random account from the game data
    account_a = account_b
    account_b = random.choice(data)
    while account_a == account_b:
        account_b = random.choice(data)

    print("Compare A:", format_data(account_a))
    print(vs)
    print("Compare B:", format_data(account_b))

    # Ask user for a guess
    guess = input("Who has more followers? Type 'A' or 'B': ").lower()

    # Check if user is correct.
    # Get the follower count of each account.
    a_follower_count = account_a["follower_count"]
    b_follower_count = account_b["follower_count"]
    is_correct = check_answer(guess, a_follower_count, b_follower_count)

    # Clear the screen between rounds.
    clear()
    print(logo)

    # Give user feedback on their guess.
    # Score tracking
    if is_correct:
        score += 1
        print(f"You're right! Current score: {score}")
    else:
        end = True
        print(f"Sorry, that's wrong. Final score: {score}")
