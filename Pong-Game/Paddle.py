from turtle import Turtle, Screen

### Class to create and control paddles for both players ###

class Paddle(Turtle):

    def __init__(self, x_position, y_position):

        super().__init__()
        self.shape("square")
        self.color("white")
        self.penup()

        ### Make paddle tall (5 units) and narrow (1 unit) ###

        self.shapesize(stretch_wid=5, stretch_len=1)
        self.goto(x_position, y_position)

    ### Move paddle upward by 20 pixels ###

    def go_up(self,):

        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)

    ### Move paddle downward by 20 pixels ###

    def go_down(self,):

        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)

    ### Assign keyboard keys to control the paddle ###

    def move(self, up_key, down_key):

        self.screen.onkey(self.go_up, f"{up_key}")
        self.screen.onkey(self.go_down, f"{down_key}")