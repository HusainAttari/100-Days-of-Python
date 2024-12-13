from tkinter import *
import pandas as pd
import random

BACKGROUND_COLOR = "#B1DDC6"
current_card = {}

# ----------------- READ WORDS -----------------

try :
	df = pd.read_csv('data/Words to learn.csv')
except FileNotFoundError :
	df = pd.read_csv('data/french_words.csv')

to_learn = df.to_dict(orient='records')
learnt = []

# ----------------- NEW CARDS -----------------

def new_card():
	global current_card, flip_timer
	root.after_cancel(flip_timer)
	current_card = random.choice(to_learn)
	card.itemconfig(title, text='French', fill='black')
	card.itemconfig(text, text=current_card["French"], fill='black')
	card.itemconfig(card_image, image=cf_image)
	flip_timer = root.after(3000, flip_card)

# ----------------- FLIP CARD -----------------

def flip_card():
	card.itemconfig(title, text='English', fill='white')
	card.itemconfig(text, text=current_card['English'], fill='white')
	card.itemconfig(card_image, image=cb_image)

# ----------------- KNOWN CARD -----------------

def is_known():
	global to_learn, learnt
	learnt.append(current_card)
	to_learn.remove(current_card)
	pd.DataFrame(to_learn).to_csv("data/Words to learn.csv", index=0)
	pd.DataFrame(learnt).to_csv('data/Words learnt.csv', index=0)
	new_card()

# ----------------- UI -----------------

root = Tk()
root.title('Flash Card App')
root.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer = root.after(3000, flip_card)

# Card
card = Canvas()
card.config(height=526, width=800, highlightthickness=0, bg=BACKGROUND_COLOR)
cf_image = PhotoImage(file='images/card_front.png')
cb_image = PhotoImage(file='images/card_back.png')
card_image = card.create_image(400, 263, image=cf_image)
title = card.create_text(400, 150, text='', font=('Arial', 40, 'italic'))
text = card.create_text(400, 263, text='', font=('Arial', 60, 'bold'))
card.grid(row=0, column=0, columnspan=2)

# Button - Correct

check_image = PhotoImage(file='images/right.png')
check_button = Button(image=check_image, highlightthickness=0, command=is_known)
check_button.grid(row=1, column=1)

# Button - Incorrect

cross_image = PhotoImage(file='images/wrong.png')
cross_button = Button(image=cross_image, highlightthickness=0, command=new_card)
cross_button.grid(row=1, column=0)

new_card()

root.mainloop()