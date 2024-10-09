from turtle import Turtle

ALIGNMENT = 'center'
FONT = ('Courier New', 14, 'normal')

class Scoreboard(Turtle):

	def __init__(self):
		super().__init__()
		self.hideturtle()
		self.pencolor('white')
		self.score = 0
		with open('data.txt') as f :
			self.highscore = int(f.read())
		self.goto(0, 270)
		self.refresh()

	def refresh(self):
		self.clear()
		self.write(f"Score : {self.score} Highscore : {self.highscore}", align=ALIGNMENT, font=FONT)

	def game_over(self):
		if self.score > self.highscore :
			with open('data.txt', 'w') as f :
				f.write(str(self.score))
			self.highscore = self.score
		self.refresh()
		self.goto(0,0)
		self.write(f"GAME OVER", align=ALIGNMENT, font=FONT)