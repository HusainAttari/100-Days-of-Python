from tkinter import *
from playsound import playsound

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 0.1
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
REPS = 0
TIMER = None

# ---------------------------- JUMP WINDOW TO FOCUS ------------------------------- #

def jump_to_top():
	window.attributes('-topmost', 1)
	window.attributes('-topmost', 0)

# ---------------------------- TIMER RESET ------------------------------- # 

def reset_timer():
	global REPS

	window.after_cancel(TIMER)
	canvas.itemconfig(time_text, text="00:00")
	title_text.config(text='Timer', fg=GREEN)
	REPS = 0
	checkmark_label.config(text="")

# ---------------------------- TIMER MECHANISM ------------------------------- # 

def start_timer():
	global REPS
	REPS += 1

	if REPS % 8 == 0 :
		title_text.config(text="Break", fg=RED)
		count_down(LONG_BREAK_MIN*60)
	elif REPS % 2 == 0 :
		title_text.config(text="Break", fg=PINK)
		count_down(SHORT_BREAK_MIN*60)
	else :
		title_text.config(text='Work', fg=GREEN)
		count_down(WORK_MIN*60)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

def count_down(count):
	global TIMER 

	mins = int(count // 60)
	secs = int(count % 60)

	if secs < 10 :
		secs = f'0{secs}'
	if mins < 10 :
		mins = f'0{mins}'

	if count >= 0 :
		canvas.itemconfig(time_text, text=f'{mins}:{secs}')
		TIMER = window.after(1000, count_down, count-1)
	else :
		jump_to_top()
		start_timer()
		marks = ""
		for _ in range(REPS // 2):
			marks += "✔"
		checkmark_label.config(text=marks)
		playsound("alarm-clock-90867.mp3")

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.config(padx=100, pady=50, bg=YELLOW)
window.title("Pomodoro Timer")

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
time_text = canvas.create_text(100, 125, text="00:00", font=(FONT_NAME, 35, "bold"), fill="white")
canvas.grid(row=1, column=1)

title_text = Label(text="Timer", font=("Poiret One", 50), fg=GREEN, bg=YELLOW)
title_text.grid(row=0, column=1)

start_button = Button(text="Start", highlightthickness=0, command=start_timer)
start_button.grid(row=2, column=0)

reset_button = Button(text="Reset", highlightthickness=0, command=reset_timer)
reset_button.grid(row=2, column=2)

checkmark_label = Label(text="", font=(FONT_NAME, 22), fg=GREEN, bg=YELLOW)
checkmark_label.grid(row=3, column=1)

window.mainloop()