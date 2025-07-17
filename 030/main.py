"""
try:
    file = open("./file.txt")
    people = {"name": "Handika"}
    print(people["nama"])
except FileNotFoundError:
    file = open("file.txt", "w")
    file.write("Halo saya saat ini sedang belajar python.")
except KeyError as error_message:
    print(f"The key {error_message} does not exist.")
else:
    content = file.read()
    print(content)
finally:
    # raise TypeError("This error message made by me:).")
    file.close()
    print("File was closed.")
"""

height = float(input("Height in M: "))
weight = int(input("Weight in Kg: "))

if height > 3:
    raise ValueError("Human height should not be over 3 meters.")

bmi = weight / height ** 2
print(bmi)