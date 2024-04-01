from turtle import Turtle
STARTING_POSITIONS_LEFT = [(-385, -20), (-385, 0), (-385, 20)]
STARTING_POSITIONS_RIGHT = [(375, -20), (375, 0), (375, 20)]
CEILING = 370
BOTTOM = -360
MOVE_DISTANCE = 20


class Paddle:

    def __init__(self, is_left=True, initial_direction="up"):
        self.squares = []
        self.create_paddle(is_left)
        self.direction = initial_direction

    def create_paddle(self, is_left):
        if is_left:
            positions = STARTING_POSITIONS_LEFT
        else:
            positions = STARTING_POSITIONS_RIGHT

        for position in positions:
            self.add_square(position)

    def add_square(self, position):
        square = Turtle()
        square.shape("square")
        square.color("white")
        square.penup()
        square.goto(position)
        self.squares.append(square)

    def move(self):
        if self.direction == "up":
            top_square_y = max(square.ycor() for square in self.squares)
            if top_square_y + MOVE_DISTANCE > CEILING:
                adjustment = CEILING - top_square_y
                for square in self.squares:
                    square.sety(square.ycor() + adjustment)
                self.set_direction_down()
            else:
                for square in self.squares:
                    square.sety(square.ycor() + MOVE_DISTANCE)

        elif self.direction == "down":
            bottom_square_y = min(square.ycor() for square in self.squares)
            if bottom_square_y - MOVE_DISTANCE < BOTTOM:
                adjustment = BOTTOM - bottom_square_y
                for square in self.squares:
                    square.sety(square.ycor() + adjustment)
                self.set_direction_up()
            else:
                for square in self.squares:
                    square.sety(square.ycor() - MOVE_DISTANCE)

    def set_direction_up(self):
        self.direction = "up"

    def set_direction_down(self):
        self.direction = "down"

