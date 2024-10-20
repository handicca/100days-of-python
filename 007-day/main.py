import random
from hangman_art import stages, logo
from hangman_word import *

from os import system, name


def clear():
    # for windows
    if name == "nt":
        _ = system("cls")
    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system("clear")


chosen_word = random.choice(word_list)

lives = 6

print(logo)

# Testing code
print(f"Pssst, the solution is {chosen_word}.")

display = []
for _ in chosen_word:
    display.append("_")

end_of_game = False

while not end_of_game:
    guess = input("Guess a letter: ").lower()
    clear()

    if guess in display:
        print(f"You've already guessed {guess}")

    for position in range(len(chosen_word)):
        if chosen_word[position] == guess:
            display[position] = guess

    if guess not in chosen_word:
        print(f"You guessed {guess}, that's not in the word. You lose a life.")
        lives -= 1

    # Join all the elements in the list and turn it into a String.
    print(f"{''.join(display)}")

    if lives == 0:
        end_of_game = True
        print("You lose")
    elif "_" not in display:
        end_of_game = True
        print("You win")

    print(stages[lives])
