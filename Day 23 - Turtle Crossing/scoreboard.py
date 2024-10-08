from turtle import Turtle 

ALIGN = 'left'
FONTS = ('Courier New', 18, 'normal')

class Scoreboard(Turtle):

	def __init__(self):
		super().__init__()
		self.ht()
		self.pu()
		self.goto(-280, 250)
		self.level = 0
		self.update()

	def update(self):
		self.level += 1
		self.clear()
		self.write(f'Level : {self.level}', align=ALIGN, font=FONTS)

	def game_over(self):
		self.goto(0,0)
		self.write('GAME OVER!', align='center', font=FONTS)