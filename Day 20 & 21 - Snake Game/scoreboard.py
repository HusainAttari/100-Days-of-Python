from turtle import Turtle

ALIGNMENT = 'center'
FONT = ('Courier New', 14, 'normal')

class Scoreboard(Turtle):

	def __init__(self):
		super().__init__()
		self.hideturtle()
		self.pencolor('white')
		self.score = 0
		self.goto(0, 270)
		self.write(f"Score : {self.score}", align=ALIGNMENT, font=FONT)
		self.refresh()

	def refresh(self):
		self.clear()
		self.write(f"Score : {self.score}", align=ALIGNMENT, font=FONT)

	def game_over(self):
		self.goto(0,0)
		self.write(f"GAME OVER", align=ALIGNMENT, font=FONT)