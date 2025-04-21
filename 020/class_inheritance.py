class Animal:
    def __init__(self):
        self.eyes = 2

    def breathe(self):
        print("Inhale, exhale")


class Fish(Animal):
    def __init__(self):
        super().__init__()

    def breathe(self):
        super().breathe()
        print("Doing this underwater")

    def swim(self):
        print("Moving in water")


nemo = Fish()
nemo.swim()
nemo.breathe()
print(nemo.eyes)


class Dog:
    def __init__(self):
        self.temperament = "loyal"


class Labrador(Dog):
    def __init__(self):
        super().__init__()
        self.temperament = "gentle"


kirik = Dog()
print(f"A dog is {kirik.temperament}")

sparky = Labrador()
print(f"Sparky is {sparky.temperament}")
