from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []
for i in question_data:
	q_obj = Question(i['text'], i['answer'])
	question_bank.append(q_obj)

quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
	quiz.next_question()

print("You\'ve completed the quiz!")
print(f"Your final score is : {quiz.score}/{quiz.question_number}")