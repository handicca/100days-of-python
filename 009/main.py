# Python Dictionaries

programming_dictionary = {
    "Bug": "An error in program that prevents the program from running as expected.",
    "Function": "A piece of code that you can easily call over and over again.",
}

"""
    key dalam dictionary bisa berupa objek apa pun yang bersifat hashable (dapat 
    di-hash). Objek yang hashable adalah objek yang memiliki nilai hash yang 
    tetap selama hidupnya. Ini berarti bahwa kunci dalam dictionary harus 
    bersifat tidak berubah (immutable). Beberapa contoh tipe data yang dapat 
    digunakan sebagai kunci dalam dictionary termasuk: String, Angka(int/float bilangan kompleks), Tuple(jika semua elemennya juga bersifat hashable), 
    boolean, dan tipe data bersifat hashable.
    
    Namun, tipe data yang bersifat mutable seperti list atau dictionary tidak 
    bisa digunakan sebagai kunci karena mereka dapat berubah nilainya setelah 
    dimasukkan ke dalam dictionary, yang akan mempengaruhi hash dan mengganggu 
    struktur internal dictionary.
"""

# Duplicate values will overwrite existing values:
car = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964,
    "year": 2000,
    "colors": ["red", "black", "blue"],
}
print(car)
# Dictionary Length
print(len(car))
print(type(car))  # <class 'dict'>

# The dict() constructor
# using keyword arguments
handika = dict(full_name="Handika Syam", birth_year=2004, is_married=False)
print(handika)
# with sequences of key-value pairs
ridho = dict([("full_name", "Ridho Syam"), ("birth_year", 1999), ("is_married", False)])
print(ridho)

# Accessing items
print(handika["full_name"])
print(ridho.get("is_married"))

# Get keys => The keys() method will return a list of all the keys in the dictionary.
print(handika.keys())

# Get values => The values() method will return a list of all the values in the dictionary.
print(handika.values())

# Get Items => The items() method will return each item in a dictionary, as tuples in a list.
print(handika.items())

# Change Values of the specific item by reffering to its key name
ridho["is_married"] = True
# The update() method will update the dictionary with the items from a given argument. If the item does not exist, the item will be added.
ridho.update({"birth_year": 2000})

# Adding items
ridho["job"] = "Programmer King JS"

# Removing items
# The pop() method removes the item with the specified key name:
ridho.pop("is_married")
# The popitem() method removes the last inserted item (in versions before 3.7, a random item is removed instead):
# ridho.popitem()
# The del keyword removes the item with the specified key name:
del ridho["birth_year"]
# The del keyword can also delete the dictionary completely:
# del ridho
# print(ridho)  #this will cause an error because "thisdict" no longer exists.
# The clear() method empties the dictionary:
ridho.clear()
print(ridho) # {}

# Loop Dictionaries https://www.w3schools.com/python/python_dictionaries_loop.asp
# Copy Dictionaries https://www.w3schools.com/python/python_dictionaries_copy.asp

# Nesting
# Nesting a List in a Dictionary
# travel_log = {
#     "Indonesia": ["Lampung", "Bangka Belitung", "Jawa Barat"],
#     "Japan": ["Tokyo", "Osaka", "Shibuya"]
# }

# Nesting a Dictionary in a Dictionary
# travel_log = {
#     "Indonesia": {"city_visited": ["Lampung", "Bangka Belitung", "Jawa Barat"], "total_visited": 3},
#     "France": {"city_visited": ["Paris", "Lille", "Dijon"]},
#     "Germany": {"city_visited": ["Berlin", "Hamburg", "Stuttgart"]},
# }

# print(travel_log["Indonesia"]["city_visited"])

# Nesting a Dictionary in a list
travel_log = [
    {
        "country": "Indonesia",
        "city_visited": ["Lampung", "Bangka Belitung", "Jawa Barat"],
        "total_visited": 3,
    },
    {
        "country": "France",
        "city_visited": ["Paris", "Lille", "Dijon"],
        "total_visited": 0,
    },
    {
        "country": "Germany",
        "city_visited": ["Berlin", "Hamburg", "Stuttgart"],
        "total_visited": 0,
    }
]
