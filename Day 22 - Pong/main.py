from turtle import Screen
from paddle import Paddle 
from ball import Ball 
from scoreboard import Scoreboard
import time

# Creating Screen object
screen = Screen()
screen.bgcolor('black')
screen.setup(height=600, width=800)
screen.title("Pong!")
screen.tracer(0) # Stop animations
screen.listen()

# Creating ball
ball = Ball()

# Creating scoreboard
sb = Scoreboard()

# Creating paddles
r_paddle = Paddle(350, 0)
l_paddle = Paddle(-350, 0)

# Paddle movements - Up & Down for right paddle, W & S for left paddle
screen.onkey(r_paddle.up, 'Up')
screen.onkey(r_paddle.down, 'Down')
screen.onkey(l_paddle.up, 'w')
screen.onkey(l_paddle.down, 's')


is_game_on = True 

while is_game_on:
	time.sleep(ball.movement_speed)
	screen.update()
	ball.move()

	# Detecting collision with top/bottom wall
	if ball.ycor() > 280 or ball.ycor() < -280 :
		ball.bounce_y()

	# Detecting collision with either paddle
	if (ball.distance(r_paddle) < 50 and ball.xcor() > 320) or (ball.distance(l_paddle) < 50 and ball.xcor() < -320) :
		ball.bounce_x()

	# Detecting when a paddle misses a ball - The ball returns to center and moves towards the other player
	if ball.xcor() > 350 :
		ball.reset()
		sb.l_point()

	if ball.xcor() < -350 :
		ball.reset()
		sb.r_point()

	# If either player scores 20, game over
	if sb.r_score == 20 or sb.l_score == 20 :
		sb.game_over()
		is_game_on = False

screen.exitonclick()