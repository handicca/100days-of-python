def greet():
    print("Hello")
    print("World")
    print("Happy")


# greet()


# Parameter adalah variabel yang tercantum di dalam tanda kurung dalam definisi fungsi.
def greeting(name):
    print(f"Hello {name}")


# Argumen adalah nilai yang dikirim ke fungsi ketika dipanggil.
greeting("Handika")

def greet_with(name, location):
    print(f"Hello {name}")
    print(f"What is it like in {location}")

# Position argument => meneruskan argument sesuai urutannya
greet_with("Handika", "Ohio")

# Keyword Argument => meneruskan argument sesuia keyword parameternya
greet_with(location="Ohio", name="Handika")
