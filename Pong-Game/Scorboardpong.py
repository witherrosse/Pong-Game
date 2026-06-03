from turtle import Turtle

### Class to track and display scores for both players ###

class Scoreboard(Turtle):

    def __init__(self):

        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.l_score = 0    # Left player score
        self.r_score = 0    # Right player score
        self.update_score()

    ### Show both scores on screen ###

    def update_score(self):

        self.goto(-100, 200)   # Left player score position
        self.write(self.l_score, align="center", font=("courier", 60, "bold"))
        self.goto(100, 200)    # Right player score position
        self.write(self.r_score, align="center", font=("courier", 60, "bold"))

    ### Increase left player score by 1 ###

    def l_point(self):

        self.l_score += 1
        self.clear()
        self.update_score()

    ### Increase right player score by 1 ###

    def r_point(self):

        self.r_score += 1
        self.clear()
        self.update_score()