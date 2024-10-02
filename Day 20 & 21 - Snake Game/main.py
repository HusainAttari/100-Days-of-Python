from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import random
import time

# Creating screen object and setting it up
screen = Screen()
screen.setup(600, 600)
screen.title("Snake Game")
screen.bgcolor("black")

# Setting screen tracer to 0 to stop animations
screen.tracer(0)

# Creating snake object
snake = Snake()

# Creating food object
food = Food()

# Creating scoreboard object
sb = Scoreboard()

# Creating a flag for while game is on
is_game_on = True

# Listen for keypresses
screen.listen()
screen.onkey(snake.up, 'Up')
screen.onkey(snake.down, 'Down')
screen.onkey(snake.right, 'Right')
screen.onkey(snake.left, 'Left')

while is_game_on:
	screen.update() # Refreshing screen to show new turtle positions
	time.sleep(0.1) # To control screen refresh rate
	snake.move()

	# Detecting when the snake eats the food
	if snake.head.distance(food) < 15 :
		sb.score += 1
		sb.refresh()
		snake.extend()
		food.refresh()

	# Detecting when snake hits walls
	if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 280 or snake.head.ycor() < -290 :
		is_game_on = False
		sb.game_over()

	# Detecting collision with body
	for segment in snake.segments[1:]:
		if snake.head.distance(segment) < 10 :
			sb.game_over()
			is_game_on = False


screen.exitonclick()