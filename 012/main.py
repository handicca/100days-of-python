# Local Scope
# A variable created inside a function belongs to the local scope of that function, and can only be used inside that function.


def drink_potion():
    # local scope
    postion_strength = 2
    print(postion_strength)


drink_potion()
# print(potion_strength) # Error


# Function Inside Function
# As explained in the example above, the variable potion_strength is not available outside the function, but it is available for any function inside the function:
"""
def myfunc():
    x = 300

    def myinnerfunc():
        print(x)

    myinnerfunc()


myfunc()
"""


# Global Scope
# A variable created in the main body of the Python code is a global variable and belongs to the global scope.
# Global variables are available from within any scope, global and local.

player_health = 10


def game():
    def potion():
        potion_strength = 2
        print(player_health)

    potion()


game()
print(player_health)


# Naming Variables

# If you operate with the same variable name inside and outside of a function, Python will treat them as two separate variables, one available in the global scope (outside the function) and one available in the local scope (inside the function):
"""
x = 300


def myfunc():
    x = 200
    print(x)


myfunc()

print(x)
"""

# Global Keyword
# If you need to create a global variable, but are stuck in the local scope, you can use the global keyword.
# The global keyword makes the variable global.
x = 300


def myfunc():
    global x
    x = 200


myfunc()

print(x)

"""
Praktik mengubah variabel global menggunakan kata kunci `global` dalam fungsi di Python dapat 
menjadi sumber kebingungan dan kompleksitas dalam kode, terutama saat aplikasi Anda tumbuh lebih 
besar
"""

# Global Constant => Variable yang nilainya tidak dapat diubah di seluruh program:
PI = 3.1415
GRAVITY = 9.81


def hitung_luas_lingkaran(jari_jari):
    return PI * jari_jari**2


def hitung_kecepatan_jatuh(waktu):
    return GRAVITY * waktu


print("Luas lingkaran dengan jari-jari 5 adalah:", hitung_luas_lingkaran(5))
print("Kecepatan jatuh setelah 2 detik adalah:", hitung_kecepatan_jatuh(2))
