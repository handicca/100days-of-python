import random
from art import logo

# Menentukan jumlah percobaan untuk setiap tingkat kesulitan
EASY_LEVEL_ATTEMPTS = 10
HARD_LEVEL_ATTEMPTS = 5

print(
    logo,
    "Welcome to the Number Guessing Game.",
    "I'm thinking of a number between 1 and 100",
    sep="\n",
)


def set_difficulty():
    level = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
    if level == "hard":
        return HARD_LEVEL_ATTEMPTS
    else:
        return EASY_LEVEL_ATTEMPTS


attempts = set_difficulty()
answer = random.randint(1, 100)

end = False
while not end:
    print(f"You have {attempts} attempts remaining to guess the number.")
    user_guess = input("Make a guess: ")

    if not user_guess.isdigit():
        print("Please enter a valid number.")
        continue

    user_guess = int(user_guess)

    if attempts == 1:
        print(
            "You've run out of guesses, You lose.",
            f"The correct answer was {answer}.",
            sep="\n",
        )
        end = True
    else:
        if user_guess > answer:
            print("Too high.", "Guess again.", sep="\n")
        elif user_guess < answer:
            print("Too low.", "Guess again.", sep="\n")
        else:
            print(f"You got it! The answer was {answer}")
            end = True

    attempts -= 1
