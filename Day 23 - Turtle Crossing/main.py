from turtle import Screen
from player import Player
from car_manager import Car
from scoreboard import Scoreboard 
import time

# Creating and setting up the screen object
screen = Screen()
screen.setup(height=600, width=600)
screen.tracer(0)

# Creating player object
player = Player()

# Creating car object
cars = Car()

# Creating scoreboard object
sb = Scoreboard()

# Player movement
screen.listen()
screen.onkey(player.move, 'Up')

is_game_on = True 

while is_game_on:
	time.sleep(0.1)
	screen.update()
	cars.create_car()
	cars.move()

	for car in cars.car_list :
		if player.distance(car) < 20 :
			is_game_on = False
			sb.game_over()

	if player.ycor() > 280 :
		cars.next_level()
		player.start_line()
		sb.update()


screen.exitonclick()