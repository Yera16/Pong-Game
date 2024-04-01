from turtle import Turtle
import time
import random

DIRECTIONS = [40, 130, 220, 310, 30, 120, 210, 300, 45, 135, 225, 315, 60, 150, 240, 330]
class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.direction = random.choice(DIRECTIONS)
        self.create_ball()

    def create_ball(self):
        self.shape("circle")
        self.color("red")
        self.penup()
        self.shapesize(stretch_len=0.8, stretch_wid=0.8)

    def move(self):
        self.setheading(self.direction)
        self.forward(11)

        if self.direction >= 360:
            self.direction -= 360

    def bounce_y(self):

        self.direction = -self.direction

    def bounce_x(self):
        if self.direction < 180:
            self.direction = 180 - self.direction
        else:
            self.direction = 540 - self.direction

    def refresh(self):
        time.sleep(0.7)
        self.home()
        self.direction = random.choice(DIRECTIONS)




