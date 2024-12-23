def greet():
    print("Hello")
    print("World")
    print("Happy")


greet()

"""
Parameter => variabel/placeholder yang berfungsi untuk menampung -
nilai yang akan dikirimkan ke dalam fungsi.
"""


def greeting(name):
    print(f"Hello {name}")


"""
Argument => Nilai sebenarnya dari data yang diberikan ke function.
"""
greeting("Handika")


# Function dengan lebih dari 1 argument
def greet_with(name, location):
    print(f"Hello {name}")
    print(f"What is it like in {location}")


# Position Argument => meneruskan argument sesuai urutannya
# greet_with('Handika', "Jebu Laut")

# Keyword Argument => meneruskan argument sesuai keyword parameternya
# greet_with(location="Jebu Laut", name="Handika")
