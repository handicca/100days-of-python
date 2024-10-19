# Random Module
import random
import my_module
from typing import List

random_integer: int = random.randint(1, 10)
print(random_integer)
print(my_module.PI)

random_float: float = random.random() * 5
print(random_float)

# Data Structure
# List
states_of_america: List[str] = [
    "Delaware",
    "Pennsylvania",
    "New Jersey",
    "Georgia",
    "Connecticut",
    "Massachusetts",
    "Maryland",
    "South Carolina",
    "New Hampshire",
    "Virginia",
    "New York",
    "North Carolina",
    "Rhode Island",
    "Vermont",
    "Kentucky",
    "Tennessee",
    "Ohio",
    "Louisiana",
    "Indiana",
    "Mississippi",
    "Illinois",
    "Alabama",
    "Maine",
    "Missouri",
    "Arkansas",
    "Michigan",
    "Florida",
    "Texas",
    "Iowa",
    "Wisconsin",
    "California",
    "Minnesota",
    "Oregon",
    "Kansas",
    "West Virginia",
    "Nevada",
    "Nebraska",
    "Colorado",
    "North Dakota",
    "South Dakota",
    "Montana",
    "Washington",
    "Idaho",
    "Wyoming",
    "Utah",
    "Oklahoma",
    "New Mexico",
    "Arizona",
    "Alaska",
    "Hawaii"]

print(states_of_america[0])
print(states_of_america[2])
print(states_of_america[-1])  # print last index from List

# Merubah value dari item list
states_of_america[1] = 'Pencilvania'
# Menambahkan item di akhir list
states_of_america.append('Fuckland')
# Menambahkan semua item dari iterable
states_of_america.extend(['Shitland', 'Cukiland'])
print(states_of_america)

# Nested List
# dirty_dozen = [
#     "Strawberries",
#     "Spinach",
#     "Kale",
#     "Nectarines",
#     "Apples",
#     "Grapes",
#     "Peaches",
#     "Cherries",
#     "Pears",
#     "Tomatoes",
#     "Celery",
#     "Potatoes"]

fruits = [
    "Strawberries",
    "Nectarines",
    "Apples",
    "Grapes",
    "Peaches",
    "Cherries",
    "Pears"]
vegetables = ["Spinach", "Kale", "Tomatoes", "Celery", "Potatoes"]

dirty_dozen = [fruits, vegetables]
print(dirty_dozen)
