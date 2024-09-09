from turtle import Turtle, Screen
import random

# Creating screen object and setting it up
screen = Screen()
screen.setup(height=500, width=600)

# Turtle colors for the race
colors = ['Purple', 'Navy', 'Blue', 'Green', 'Yellow', 'Orange', 'Red']

# Y-coordinates for starting line
y = [0, 70, -70, 140, -140, 210, -210]

# List of turtles in the race
turtle_list = []

# Flag for starting and ending race
is_race_on = False

# Taking user's bet
user_bet = screen.textinput(title='Place your bet!', prompt='Choose a color [Purple/Navy/Blue/Green/Yellow/Orange/Red] :')
is_race_on = True

for i in range(len(colors)):
	new_turtle = Turtle(shape='turtle')
	new_turtle.color(colors[i])
	new_turtle.penup()
	new_turtle.goto(x=-260, y=y[i])
	turtle_list.append(new_turtle)

while is_race_on:
	for turtle in turtle_list:
		if turtle.xcor() >= 260:
			print(f"You won! The {turtle.pencolor()} turtle came first!") if turtle.pencolor() == user_bet else print(f"You lost! The {turtle.pencolor()} turtle came first!")
			is_race_on = False

		turtle.fd(random.randint(0,10))

screen.exitonclick()