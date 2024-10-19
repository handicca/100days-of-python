import random
from ascii_art import *

# Write your code below this line 👇

ascii_art_choices = [rock, paper, scissors]

user_choice = int(
    input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))

if user_choice < 0 or user_choice > 2:
    print("You typed an invalid number, You lose!")
else:
    print(f"You chose:\n{ascii_art_choices[user_choice]}")

    # Generate computer's choice
    computer_choice = random.randint(0, 2)
    print(f"Computer chose:\n{ascii_art_choices[computer_choice]}")

    # Determine the winner
    if user_choice == computer_choice:
        print("It's a draw.")
    elif ((user_choice == 0 and computer_choice == 2) or (user_choice == 1 and computer_choice == 0)
          or (user_choice == 2 and computer_choice == 1)):
        print("You win!")
    else:
        print("You lose:(")
