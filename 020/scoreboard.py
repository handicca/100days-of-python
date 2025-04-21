from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.hideturtle()
        self.teleport(0, 270)
        self.update_score()

    def update_score(self):
        self.write(f"Score: {self.score}", align="center", font=("Courier", 16, "normal"))

    def game_over(self):
        self.teleport(0, 0)
        self.write("GAME OVER!", align='center', font=("Courier", 16, "normal"))

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_score()