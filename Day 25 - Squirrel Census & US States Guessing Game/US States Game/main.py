import turtle
import pandas as pd 

screen = turtle.Screen()
screen.title('U.S. States Game')

image = 'blank_states_img.gif'
screen.addshape(image)
turtle.shape(image)

states = pd.read_csv('50_states.csv')
user_correct_answer = []
state_list = states['state'].to_list()

while len(user_correct_answer) < len(state_list) :
	user_answer = screen.textinput(title=f"{len(user_correct_answer)}/{len(states['state'])} guessed", prompt="What's another state's name?").title()
	
	if (user_answer in state_list) and (user_answer not in user_correct_answer):
		user_correct_answer.append(user_answer)
		row = states[states['state'] == user_answer]
		cords = (row['x'].item(), row['y'].item())
		text = turtle.Turtle()
		text.ht()
		text.pu()
		text.goto(cords)
		text.write(user_answer)

	if user_answer == 'Exit' :
		missed_states = []
		for x in state_list :
			if x not in user_correct_answer :
				missed_states.append(x)
		new_data = pd.DataFrame(missed_states)
		new_data.to_csv('states_to_learn.csv', index=False)

		break

screen.exitonclick()