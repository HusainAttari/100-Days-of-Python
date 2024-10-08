from turtle import Turtle 

ALIGN = 'center'
FONTS = ('Courier New', 26, 'normal')

class Scoreboard(Turtle):

	def __init__(self):
		super().__init__()
		self.color('white')
		self.ht()
		self.pu()
		self.r_score = 0
		self.l_score = 0
		self.update_scoreboard()

	def update_scoreboard(self):
		self.clear()
		self.goto(-50,235)
		self.write(self.l_score, align=ALIGN, font=FONTS)
		self.goto(0,235)
		self.write(":", align=ALIGN, font=FONTS)
		self.goto(50,235)
		self.write(self.r_score, align=ALIGN, font=FONTS)

	def r_point(self):
		self.r_score += 1
		self.update_scoreboard()

	def l_point(self):
		self.l_score += 1
		self.update_scoreboard()

	def game_over(self):
		self.goto(0, 100)
		self.write('GAME OVER!', align=ALIGN, font=FONTS)