import json
import os

MENU = {}
SUPPLIES = {
	'Money': 0
}

nextCustomer = True #Flag for loop
password = "MonkeyCoffee" # Password to access admin commands
menuBook = 'Menu.json' 
fridge = 'supplies.json'

# Commands and Actions
public_cmd = {
	'help': 'A list of all commands',
	'menu': 'Display the menu',
	'order': 'Order an item off the menu',
}
admin_cmd = {
	'addToMenu': 'Add items to the menu',
	'restock': 'Restock supplies',
	'report': 'Give a report of available supplies',
	'removeFromMenu': 'Remove an item from the menu'
}

# Check if menu/supply catalog already exists, and create an empty menu/supply catalog if not
if not os.path.exists(menuBook):
	with open(menuBook, 'w') as m:
		json.dump(MENU, m, indent=4)
	with open(fridge, 'w') as f:
		json.dump(SUPPLIES, f, indent=4)
else:
	with open(menuBook, 'r', encoding='utf8') as m:
		MENU = json.load(m)
	with open(fridge, 'r', encoding='utf8') as f:
		SUPPLIES = json.load(f)

# Add items to the menu
def addToMenu():
	ing = {}
	name = input("What item would you like to add to the menu?: ")
	print("Enter the ingredient(s) and their quantity when prompted. When finished, enter 'STOP' as ingredient name.")
	while True:
		ingredient = input("Ingredient: ")
		if ingredient.lower() == "STOP".lower():
			break
		quantity = float(input(f'How much {ingredient.lower()} will be required?: '))
		ing[ingredient] = quantity
		if ingredient not in SUPPLIES:
			SUPPLIES[ingredient] = 0
	price = float(input(f'How much do you want {name} to cost?: '))
	item = {
	"item": name,
	"ingredients": ing,
	"cost": price
	}
	MENU[str(len(MENU)+1)] = item
	with open(menuBook, 'w') as m:
		json.dump(MENU, m, indent=4)
	with open(fridge, 'w') as f:
		json.dump(SUPPLIES, f, indent=4)


# Restock the resources
def restock():
	resource = input("What resource would you like to restock?: ")
	if resource in SUPPLIES:
		q = float(input("How much would you like to restock?: "))
		SUPPLIES[resource] += q
		with open(fridge, 'w') as f:
			json.dump(SUPPLIES, f, indent=4)		
		print(f'{q} of {resource} is added!')
	else:
		print(f"Incorrect ingredient name! No items on the menu require {resource.lower()}!")

# Order an item from the menu
def order():
	global SUPPLIES # Declaring SUPPLIES as a global variable
	if input("Would you like to browse through the menu before ordering? [Y/N]: ").lower() == 'y':
		for k in MENU:
			print(f"{k}. {MENU[k]['item']} - ${MENU[k]['cost']}")		
	item = input("What would you like to order? [Enter the item code]: ")
	if item in MENU:
		cost = MENU[item]['cost']
		cash = float(input(f"Please pay ${cost}: "))
		if cash > cost:
			print(f"Your change is: ${cash - cost}")
		elif cash < cost:
			print("Not enough money :(")
			return
		else:
			print("Thank you for paying the exact change!")
		SUPPLIES['Money'] += cost
		x = MENU[item]['ingredients']
		for key, value in x.items():
			if SUPPLIES[key]>value:
				SUPPLIES[key] -= value
			else:
				with open(fridge, 'r', encoding='utf8') as f:
					SUPPLIES = json.load(f)
				print(f"Oops! We do not have enough {key.lower()} in our supplies :(\n Please ask an admin to restock!")
				return
		with open(fridge, 'w') as f:
			json.dump(SUPPLIES, f, indent=4)
		print(f"Here's your {item.lower()}! Enjoy your visit :)")
	else:
		print("The item code you entered is invalid. Please try again :(")
		return

# help menu - dictionary of commands
def helpCommands():
	print('Public Commands -')
	for k in public_cmd:
		print(f"{k} - {public_cmd[k]}")
	print('Admin Commands -')
	for k in admin_cmd:
		print(f"{k} - {admin_cmd[k]}")

# Remove an item from the menu
def removeFromMenu(menu):
	for k in MENU:
		print(f"{k}. {MENU[k]['item']} - ${MENU[k]['cost']}")
	item = input('What item do you want to remove from the menu? Please enter the item code: ')
	if item in menu:
		del menu[item]
	else:
		print("No such item exists :(")
		return menu
	new_menu = {}
	for i, (key, value) in enumerate(menu.items(), start=1):
		new_menu[str(i)] = value
	return new_menu

# Loop to keep the program running after 1 interaction
while nextCustomer:
	os.system('cls')
	print("Welcome to The MonkeyBar Cafe!")
	if len(MENU) == 0:
		print('The menu doesn\'t exist. Please add at least one item to the menu.')
		addToMenu()
		os.system('cls')
	command = input("What can I do for you? Please type 'help' for a list of all commands: ")
	# Admin Command Handling
	if command in admin_cmd:
		command = command.lower()
		if input("This is an admin command. Please enter the password to proceed: ") == password:		
			if command == 'addtomenu':
				addToMenu() 
			if 	command == 'restock':
				restock()
			if command == 'report':
				for i,k in enumerate(SUPPLIES):
					print(f"{i+1}. {k}: {SUPPLIES[k]}")
			if command == 'removefrommenu':
				MENU = removeFromMenu(MENU)
				with open(menuBook, 'w') as m:
					json.dump(MENU, m, indent=4)
		else:
			print("Incorrect password! You cannot access this command!")
	# Public Command Handling
	elif command in public_cmd:
		command = command.lower()
		if command == 'menu':
			for k in MENU:
				print(f"{k}. {MENU[k]['item']} - ${MENU[k]['cost']}")
		if command == 'help':
			helpCommands()
		if command == 'order':
			order()
	else:
		print('The command you entered does not exist :(')
	if input("Press any key to continue or enter STOP to exit: ").lower() == 'stop':
		nextCustomer = False
		print("Thank you for visiting The MonkeyBar Cafe! Hope to see you again soon!")