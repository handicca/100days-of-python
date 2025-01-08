import art

alphabet = [
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


def caesar(start_text, shift_amount, chiper_direction):
    result = []
    if chiper_direction == "decode":
        # untuk menghasilkan minus pada shift_amount
        shift_amount *= -1
    for char in start_text:
        if char not in alphabet:
            # Jika karakter bukan huruf, tambahkan langsung
            result.append(char)
        else:
            position = alphabet.index(char)
            # Gunakan modulus untuk menjaga new_position tetap dalam rentang
            new_position = (position + shift_amount) % len(alphabet)
            result.append(alphabet[new_position])

    print(f"The {chiper_direction}d text is {''.join(result)}")


print(art.logo)

end = False
while not end:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n")
    shift = int(input("Type the shift number:\n"))
    caesar(start_text=text, shift_amount=shift, chiper_direction=direction)

    ask_continue = input(
        "Type 'yes' if you want to go again. Otherwise type 'no':\n"
    ).lower()

    if ask_continue == "no":
        end = True
