from typing import Union

# Python type hints
# Variables
name: str
name = "tung tung tung sahur"
age: int = 20
height: float = 2.8
is_anomali: bool = True

# For collections on Python 3.9+, the type of the collection item is in brackets
x: list[int] = [1, 2, 3, 4, 5]
x: set[int] = {6, 7, 7, 8, 9}

# For mappings, we need the types of both keys and values
x: dict[str, float] = {"field": 3.14}

# For tuples of fixed size, we specify the types of all the elements
x: tuple[int, str, float] = (1, "yes", 2.0)

# For tuples of variable size, we use one type and ellipsis
x: tuple[int, ...] = (1, 2, 3)

# On Python 3.10+, use the | operator when something could be one of a few types
x: list[int | str] = [3, 5, "test", "fun"]

# On earlier versions, use Union
x: list[Union[int, str]] = [3, 5, "test", "fun"]

# Functions
def stringify(num: int) -> str:
    return str(num)

def add(num1: int, num2: int) -> int:
    return num1 + num2