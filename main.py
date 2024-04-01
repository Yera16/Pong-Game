from turtle import Screen
from paddle import Paddle
from scoreboard import ScoreBoard
from ball import Ball
import time

screen = Screen()
screen.setup(width=800, height=800)
screen.bgcolor("black")
screen.title("Pong Game")
screen.tracer(0)

score_board = ScoreBoard()

screen.listen()
paddle_left = Paddle(is_left=True, initial_direction="up")
paddle_right = Paddle(is_left=False, initial_direction="up")
ball = Ball()
screen.onkey(paddle_left.set_direction_up, "w")
screen.onkey(paddle_left.set_direction_down, "s")

screen.onkey(paddle_right.set_direction_up, "Up")
screen.onkey(paddle_right.set_direction_down, "Down")

still_playing = True
while still_playing:
    screen.update()
    time.sleep(0.05)
    paddle_left.move()
    paddle_right.move()

    ball.move()

    if ball.ycor() > 365 or ball.ycor() < -365:
        ball.bounce_y()

    collision_with_right = False
    for square in paddle_right.squares:
        if 10 < ball.distance(square) < 22 and ball.xcor() > 365:
            collision_with_right = True
            break

    collision_with_left = False
    for square in paddle_left.squares:
        if 10 < ball.distance(square) < 25 and ball.xcor() > -370:
            collision_with_right = True
            break

    if collision_with_right or collision_with_left:
        ball.bounce_x()

    if ball.xcor() > 400:
        ball.refresh()
        score_board.change_score1()
    elif ball.xcor() < -405:
        ball.refresh()
        score_board.change_score2()




screen.exitonclick()