from turtle import Turtle, Screen
from Scorboardpong import Scoreboard
from Ball import Ball
from Paddle import Paddle
import time

### Setup the game window ###

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)      
screen.listen()



paddle_r = Paddle(350, 0)
paddle_l = Paddle(-350, 0)


paddle_l.move("w", "s")   
paddle_r.move("r", "f")   



ball = Ball()
scoreboard = Scoreboard()



is_game_on = True

while is_game_on:

    time.sleep(ball.move_speed)   # Control game speed

    screen.update()
    ball.move()

   

    if ball.ycor() > 280 or ball.ycor() < -280:

        ball.bounce_y()

   

    if ball.distance(paddle_r) < 50 and ball.xcor() > 320 or ball.distance(paddle_l) < 50 and ball.xcor() < -320:

        ball.bounce_x()

    

    if ball.xcor() > 380:
        
        ball.reset_position()
        scoreboard.l_point()

    

    if ball.xcor() < -380:
        
        ball.reset_position()
        scoreboard.r_point()

screen.exitonclick()
