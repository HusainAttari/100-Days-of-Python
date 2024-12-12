from tkinter import *
from tkinter import messagebox
import json
from random import randint, choice, shuffle
import pyperclip

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def generate_password():

	password_entry.delete(0, END)

	letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
	numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
	symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

	password_letters = [choice(letters) for _ in range(randint(8, 10))]
	password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
	password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

	password_list = password_letters + password_symbols + password_numbers
	shuffle(password_list)
	final_password = "".join(password_list)

	password_entry.insert(0, final_password)
	pyperclip.copy(final_password)


# ---------------------------- SAVE PASSWORD ------------------------------- #

def save_info():

	website = website_entry.get()
	user_id = user_id_entry.get()
	password = password_entry.get()

	details = {
		website : {
			"user_id" : user_id,
			"password" : password
		}	
	}

	if len(website) == 0 :
		messagebox.showerror(title="ERROR!", message="The website field cannot be left empty!")
		return

	if len(user_id) == 0 :
		messagebox.showerror(title="ERROR!", message="The username / email field cannot be left empty!")
		return

	if len(password) == 0 :
		messagebox.showerror(title="ERROR!", message="The password field cannot be left empty!")
		return

	confirmation = messagebox.askokcancel(title=website, message=f"Username : {user_id}\nPassword : {password}\nPress okay to confirm your input.")

	if confirmation :
		try :
			with open('password database.json', 'r') as f :
				data = json.load(f)
				data.update(details)
		except FileNotFoundError :
			with open('password database.json', 'w') as f :
				json.dump(details, f, indent=4)
		else :
			with open('password database.json', 'w') as f :
				json.dump(data, f, indent=4)
		finally :
			website_entry.delete(0, END)
			user_id_entry.delete(0, END)
			password_entry.delete(0, END)

# ---------------------------- SEARCH PASSWORD ------------------------------- #

def search_password() :

	website = website_entry.get()
	
	if len(website) == 0 :
		messagebox.showerror("Please enter a website to look up the details for")
		return

	try :
		with open('password database.json', 'r') as f :
			database = json.load(f)
	except FileNotFoundError :
		messagebox.showerror("No Data File Found")
	else :
		if website in database :
			user_id = database[website]['user_id']
			password = database[website]['password']
			messagebox.showinfo(title=website, message=f'Username : {user_id}\nPassword : {password}')
		else :
			messagebox.showerror("No details for this website exist")

# ---------------------------- UI SETUP ------------------------------- #

root = Tk()
root.title('Password Manager')
root.config(padx=50, pady=50)

canvas = Canvas(height=200, width=200)
logo_img = PhotoImage(file='logo.png')
logo = canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1)

website_text = Label(text="Website")
website_text.grid(row=1, column=0)

website_entry = Entry(width=21)
website_entry.grid(row=1, column=1, columnspan=1)
website_entry.focus()

search_button = Button(text="Search", command=search_password, width=15)
search_button.grid(row=1, column=2)

user_id_text = Label(text="Email / Username")
user_id_text.grid(row=2, column=0)

user_id_entry = Entry(width=40)
user_id_entry.grid(row=2, column=1, columnspan=2)

password_text = Label(text="Password")
password_text.grid(row=3, column=0)

password_entry = Entry(width=21)
password_entry.grid(row=3, column=1)

generate_pass_button = Button(text="Generate Password", command=generate_password)
generate_pass_button.grid(row=3, column=2)

add_button = Button(text="Add", width=36, command=save_info)
add_button.grid(row=4, column=1, columnspan=2)

root.mainloop()