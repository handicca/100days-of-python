from art import *


def caesar(text: str, shift_amount: int, cipher_direction: str) -> str:
    result = []
    if cipher_direction == "decode":
        shift_amount *= -1

    for char in text:
        if char.isalpha():  # Cek jika karakter adalah huruf
            # Tentukan batas (A-Z atau a-z)
            ascii_offset = 65 if char.isupper() else 97
            # Hitung posisi baru dengan operasi mod 26
            new_char = chr(
                ((ord(char) - ascii_offset + shift_amount) % 26) + ascii_offset
            )
            result.append(new_char)
        else:
            result.append(char)  # Biarkan karakter non-huruf tetap sama

    return "".join(result)


print(logo)

again = True
while again:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    message = input("Type your message:\n")
    shift = int(input("Type the shift number:\n"))

    encrypted_message = caesar(
        text=message, shift_amount=shift, cipher_direction=direction
    )
    print(f"The {direction}d text is: {encrypted_message}")

    ask_again = input(
        "Type 'yes' if you want to go again. Otherwise type 'no', default 'yes':\n"
    ).lower()
    if ask_again == "no":
        again = False
