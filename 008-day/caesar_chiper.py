from art import *

alphabet: list[str] = [
    "a",
    "b",
    "c",
    "d",
    "e",
    "f",
    "g",
    "h",
    "i",
    "j",
    "k",
    "l",
    "m",
    "n",
    "o",
    "p",
    "q",
    "r",
    "s",
    "t",
    "u",
    "v",
    "w",
    "x",
    "y",
    "z",
    "A",
    "B",
    "C",
    "D",
    "E",
    "F",
    "G",
    "H",
    "I",
    "J",
    "K",
    "L",
    "M",
    "N",
    "O",
    "P",
    "Q",
    "R",
    "S",
    "T",
    "U",
    "V",
    "W",
    "X",
    "Y",
    "Z",
]


def caesar(text: str, shift_amount: int, chiper_direction: str) -> None:
    result = []
    if chiper_direction == "decode":
        shift_amount *= -1
    for char in text:
        if char not in alphabet:
            result.append(char)
        else:
            position = alphabet.index(char)
            new_position = (position + shift_amount) % len(alphabet)
            result.append(alphabet[new_position])

    print(f"The {chiper_direction}d text is {''.join(result)}")


print(logo)

again: bool = True
while again:
    direction = input(
        "Type 'encode' to encrypt, type 'decode' to decrypt:\n"
    ).lower()
    message = input("Type your message:\n")
    shift = int(input("Type the shift number:\n"))
    caesar(text=message, shift_amount=shift, chiper_direction=direction)

    ask_again = input(
        "Type 'yes' if you want to go again. Otherwise type 'no', default 'yes':\n"
    ).lower()
    if ask_again == "no":
        again = False
