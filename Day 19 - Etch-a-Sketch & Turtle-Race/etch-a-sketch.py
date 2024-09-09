import turtle

# Creating turtle and screen objects
henry = turtle.Turtle()
screen = turtle.Screen()

def w():
	henry.fd(10)
def a():
	henry.lt(10)
def d():
	henry.rt(10)
def s():
	henry.bk(10)
def c():
	henry.reset()

screen.onkey(w, "w")
screen.onkey(a, "a")
screen.onkey(s, "s")
screen.onkey(d, "d")
screen.onkey(c, "c")

screen.listen()
screen.exitonclick()