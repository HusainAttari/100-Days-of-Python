from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"

class QuestionInterface :

	def __init__(self, QuizBrain: QuizBrain):
		self.quiz = QuizBrain

		self.window = Tk()
		self.window.title("Quizzler!")
		self.window.config(padx=20, pady=20, bg=THEME_COLOR)

		self.score_label = Label(text="Score : 0", bg=THEME_COLOR, fg='white')
		self.score_label.grid(row=0, column=1)

		self.canvas = Canvas(height=250, width=300, bg='white', highlightthickness=0, border=0)
		self.question_text = self.canvas.create_text(
			150,
			125, 
			width=280,
			text='Some question text', 
			fill=THEME_COLOR,
			font=('Arial', 20, "italic"),
			justify='center'
			)
		self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

		true_image = PhotoImage(file='images/true.png')
		self.true_button = Button(image=true_image, highlightthickness=0, command=self.true)
		self.true_button.grid(row=2, column=0)

		false_image = PhotoImage(file="images/false.png")
		self.false_button = Button(image=false_image, highlightthickness=0, command=self.false)
		self.false_button.grid(row=2, column=1)

		self.get_next_question()

		self.window.mainloop()

	def get_next_question(self):
		self.canvas.config(bg='white')
		if self.quiz.still_has_questions():
			self.score_label.config(text=f"Score: {self.quiz.score}")
			self.canvas.itemconfig(self.question_text, text=self.quiz.next_question())
		else :
			self.score_label.config(text="")
			self.canvas.itemconfig(self.question_text, text=f"You have reached the end of the quiz!\nScore: {self.quiz.score}")
			self.true_button.config(state='disabled')
			self.false_button.config(state='disabled')
	def true(self):
		self.give_feedback(self.quiz.check_answer("true"))

	def false(self):
		self.give_feedback(self.quiz.check_answer("false"))

	def give_feedback(self, is_correct: bool):
		if is_correct :
			self.canvas.config(bg="#b0e8a2")
		else :
			self.canvas.config(bg="#e8a2a2")
		self.window.after(1000, self.get_next_question)