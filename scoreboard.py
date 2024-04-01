from turtle import Turtle
ALIGNMENT = "center"
SCORE_ALIGNMENT = [(-35, 330), (35, 330)]
FONT = ("Courier", 40, "bold")


class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.score1 = 0
        self.score2 = 0
        self.penup()
        self.draw_dash()
        self.hideturtle()
        self.color("white")
        self.write_score()

    def write_score(self):
        self.goto(SCORE_ALIGNMENT[0])
        self.write(arg=self.score1, align=ALIGNMENT, font=FONT)

        self.goto(SCORE_ALIGNMENT[1])
        self.write(arg=self.score2, align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write(arg="GAME OVER!", align=ALIGNMENT, font=FONT)

    def change_score1(self):
        self.score1 += 1
        self.clear()
        self.write_score()

    def change_score2(self):
        self.score2 += 1
        self.clear()
        self.write_score()

    def draw_dash(self):
        for i in range(380, -380, -35):
            dash = Turtle()
            dash.penup()
            dash.shapesize(stretch_wid=1.1, stretch_len=0.3)
            dash.shape("square")
            dash.color("white")

            dash.setposition(0, i)


