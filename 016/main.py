"""
from turtle import Turtle, Screen

loreng = Turtle()
print(loreng)
loreng.shape('turtle')
loreng.color("blue")
loreng.forward(100)

my_screen = Screen()
my_screen.exitonclick()
"""

from prettytable import PrettyTable

table = PrettyTable()
table.add_column("Pokemon Name", ["Pikachu", "Squirtle", "Charmander"])
table.add_column("type", ["Electric", "Water", "Fire"])
table.align = "l"


print(table)
