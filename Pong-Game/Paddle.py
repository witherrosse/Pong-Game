from turtle import Turtle, Screen



class Paddle(Turtle):
    
    ''' create and control paddles for both players '''

    def __init__(self, x_position, y_position):

        super().__init__()
        self.shape("square")
        self.color("white")
        self.penup()

        

        self.shapesize(stretch_wid=5, stretch_len=1)
        self.goto(x_position, y_position)

    

    def go_up(self,):

        ''' Move paddle upward by 20 pixels '''
        
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)

    

    def go_down(self,):

        ''' Move paddle downward by 20 pixels '''

        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)

    

    def move(self, up_key, down_key):

        ''' Assign keyboard keys to control the paddle '''

        self.screen.onkey(self.go_up, f"{up_key}")
        self.screen.onkey(self.go_down, f"{down_key}")
