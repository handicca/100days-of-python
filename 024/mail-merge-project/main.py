PLACEHOLDER = "[NAME]"

with open("./input/invited_names.txt", "r") as names_file:
    names = names_file.readlines()

with open("./input/letter.txt", "r") as letter_file:
    letter_content = letter_file.read()

for name in names:
    fix_name = name.strip()
    letter = letter_content.replace(PLACEHOLDER, fix_name)
    with open(f"./output/letter_for_{fix_name}.txt", "w") as new_letter:
        new_letter.write(letter)

# TODO: Create a letter using starting_letter.txt
# for each name in invited_names.txt
# Replace the [name] placeholder with the actual name.
# Save the letters in the folder "ReadyToSend".

# Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
# Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
# Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp