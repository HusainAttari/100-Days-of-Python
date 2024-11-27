from tkinter import *

def calculate() :
	miles = int(input1.get())
	km = round(miles*1.609344)
	text4 = Label(text=km)
	text4.grid(row=2, column=1)
	
window = Tk()
window.title("Miles to Km Converter")
window.minsize(width=150, height=100)
window.config(padx=20, pady=20)

input1 = Entry(width=7)
input1.grid(row=1, column=1)

text2 = Label(text='Miles')
text2.grid(row=1, column=2)

text3 = Label(text="Km")
text3.grid(row=2, column=2)

text5 = Label(text="equals to")
text5.grid(row=2, column=0)

button1 = Button(text="Calculate", command=calculate)
button1.grid(row=3, column=1)

window.mainloop()