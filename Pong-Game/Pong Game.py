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
screen.tracer(0)      ### Turn off automatic animation ###
screen.listen()

### Create paddles for right and left player ###

paddle_r = Paddle(350, 0)
paddle_l = Paddle(-350, 0)

### Set keyboard controls for each paddle ###
paddle_l.move("w", "s")   # Left paddle: W = up, S = down
paddle_r.move("r", "f")   # Right paddle: R = up, F = down

### Create ball and scoreboard ###

ball = Ball()
scoreboard = Scoreboard()

### Main game loop ###

is_game_on = True
while is_game_on:

    time.sleep(ball.move_speed)   # Control game speed

    screen.update()
    ball.move()

    ### Bounce ball off top or bottom wall ###

    if ball.ycor() > 280 or ball.ycor() < -280:

        ball.bounce_y()

    ### Bounce ball off paddles ###

    if ball.distance(paddle_r) < 50 and ball.xcor() > 320 or ball.distance(paddle_l) < 50 and ball.xcor() < -320:

        ball.bounce_x()

    ### Right player scores when ball goes past left side ###

    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.l_point()

    ### Left player scores when ball goes past right side ###

    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.r_point()

screen.exitonclick()