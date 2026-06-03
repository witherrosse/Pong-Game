from turtle import Turtle

class Ball(Turtle):

    def __init__(self):

        super().__init__()

        self.shape("circle")
        self.color("white")
        self.penup()
        self.x_move = 10    ### Speed in x direction ###
        self.y_move = 10    ### Speed in y direction ###
        self.move_speed = 0.1   ### Delay for game speed ###

    ### Move the ball by adding speed to position ###

    def move(self):

        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    ### Reverse vertical direction when hitting top or bottom ###

    def bounce_y(self):

        self.y_move *= -1

    ### Reverse horizontal direction when hitting paddle ##

    ### Make the ball faster each time ###

    def bounce_x(self):

        self.x_move *= -1
        self.move_speed *= 0.9

    ### Reset ball to center after a player scores ###

    def reset_position(self):

        self.goto(0, 0)
        self.move_speed = 0.1
        self.bounce_x()   ### Send ball toward the other player ###