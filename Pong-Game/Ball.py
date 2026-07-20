from turtle import Turtle

class Ball(Turtle):

    def __init__(self):

        super().__init__()

        self.shape("circle")
        self.color("white")
        self.penup()
        self.x_move = 10    
        self.y_move = 10    
        self.move_speed = 0.1   ### Delay for game speed ###

    

    def move(self):

        ''' Move the ball by adding speed to position '''

        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    

    def bounce_y(self):

        ''' Reverse vertical direction when hitting top or bottom '''

        self.y_move *= -1

    
    def bounce_x(self):

        ''' Reverse horizontal direction when hitting paddle and
            Make the ball faster each time '''

        self.x_move *= -1
        self.move_speed *= 0.9

   

    def reset_position(self):
        ''' Reset ball to center after a player scores '''

        self.goto(0, 0)
        self.move_speed = 0.1
        self.bounce_x()   
