from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard

screen = Screen()
screen.title("Pong Game Py")
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.tracer(0)

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))

ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")


def game_loop():
    screen.update()
    ball.move()

    # Bounce wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # Bounce with right paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320:
        ball.setx(320)  # geser keluar dari paddle
        ball.bounce_x()

    # Bounce with left paddle
    if ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.setx(-320)
        ball.bounce_x()

    # Right miss
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.l_point()

    # Left miss
    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.r_point()

    # Panggil loop lagi setelah jeda# delay 20 ms (~50 FPS)
    screen.ontimer(game_loop, int(ball.move_speed * 1000))


# Mulai loop pertama
game_loop()

screen.mainloop()
