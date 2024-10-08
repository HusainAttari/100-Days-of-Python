from turtle import Turtle

class Paddle(Turtle):

	def __init__(self, x, y):
		super().__init__()
		self.color('white')
		self.shape('square')
		self.pu()
		self.shapesize(stretch_wid=5, stretch_len=1)
		self.goto(x, y)

	def up(self):
		self.goto(self.xcor(), self.ycor() + 20)

	def down(self):
		self.goto(self.xcor(), self.ycor() - 20)
