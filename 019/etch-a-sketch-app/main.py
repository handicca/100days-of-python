from turtle import Turtle, Screen

"""
Higher order function => function yang memanggil function lain dan function yang di panggila dinamakan callback.
"""

pen = Turtle()
screen = Screen()


def move_forwards():
    pen.fd(10)


def move_backwards():
    pen.backward(10)


def turn_right():
    pen.right(10)


def turn_left():
    pen.left(10)


def clear_sketch():
    pen.penup()
    pen.home()
    pen.clear()
    pen.pendown()


screen.onkey(fun=move_forwards, key="Up")
screen.onkey(fun=move_backwards, key="Down")
screen.onkey(fun=turn_right, key="Right")
screen.onkey(fun=turn_left, key="Left")

screen.onkey(fun=move_forwards, key="w")
screen.onkey(fun=move_backwards, key="s")
screen.onkey(fun=turn_right, key="d")
screen.onkey(fun=turn_left, key="a")

screen.onkey(fun=clear_sketch, key="c")

screen.listen()
screen.exitonclick()
