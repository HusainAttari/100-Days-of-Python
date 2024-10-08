from turtle import Turtle 
import random

COLORS = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class Car:

	def __init__(self):
		self.car_list = []
		self.move_distance = STARTING_MOVE_DISTANCE

	def create_car(self):
		if random.randint(0, 6) == 1 :
			a = Turtle('square')
			a.pu()
			a.shapesize(stretch_len=2, stretch_wid=1)
			a.color(random.choice(COLORS))
			random_y = random.randint(-240, 240)
			a.goto(300, random_y)
			self.car_list.append(a)

	def move(self):
		for car in self.car_list[:] :
			car.backward(self.move_distance)

			if car.xcor() < -320 :
				car.ht()
				self.car_list.remove(car)
				del car 

	def next_level(self):
		self.move_distance += MOVE_INCREMENT

