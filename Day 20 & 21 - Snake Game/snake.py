from turtle import Turtle

STARTING_POS = [(0,0), (-20,0), (-40,0)]
MOVING_DISTANCE = 20
UP = 90
LEFT = 180
DOWN = 270
RIGHT = 0

class Snake:

	def __init__(self):
		self.segments = []
		self.create_snake()
		self.head = self.segments[0]

	def create_snake(self):
		for position in STARTING_POS:
			self.add_segment(position)

	def add_segment(self, position):
		jerry = Turtle(shape="square")
		jerry.color("white")
		jerry.penup()
		jerry.goto(position)
		self.segments.append(jerry)

	def extend(self):
		self.add_segment(self.segments[-1].pos())

	def move(self):
		for i in range(len(self.segments)-1, 0, -1):
			cords = self.segments[i-1].pos()
			self.segments[i].goto(cords)
		self.head.fd(MOVING_DISTANCE)

	def up(self):
		if self.head.heading() != DOWN:
			self.head.setheading(UP)

	def down(self):
		if self.head.heading() != UP:
			self.head.setheading(DOWN)

	def right(self):
		if self.head.heading() != LEFT:
			self.head.setheading(RIGHT)

	def left(self):
		if self.head.heading() != RIGHT:
			self.head.setheading(LEFT)		