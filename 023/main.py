from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.title("Turtle Crossing")
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(player.go_up, 'w')
screen.onkey(player.go_up, 'Up')


def game_loop():
    screen.update()
    car_manager.create_car()
    car_manager.move_cars()

    # Detect collision with car
    for car in car_manager.all_cars:
        if car.distance(player) < 20:
            scoreboard.game_over()
            return

    # Detect car is finist
    if player.is_finish():
        player.go_to_start()
        car_manager.level_up()
        scoreboard.increase_level()

    screen.ontimer(game_loop, 20)

game_loop()

screen.mainloop()