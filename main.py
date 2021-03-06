"""
This is the Template Repl for Python with Turtle.

Python with Turtle lets you make graphics easily in Python.

Check out the official docs here: https://docs.python.org/3/library/turtle.html
"""

# DO NOT DELETE THE BELOW CODE
import turtle
t = turtle.Turtle()
t.shape('turtle') 
# DO NOT DELETE THE ABOVE CODE
t.penup()
t.goto(-380,190)
t.pendown()
t.fillcolor('cyan')

#draw squer multicolor sides
t.color('yellow')
t.forward(150)
t.left(90)
t.color('green')
t.backward(150)
t.left(90)
t.color('red')
t.forward(150)
t.left(90)
t.color('blue')
t.backward(150)
t.forward(150)

#draw Rectangle 
t.penup()
t.goto(-140,0)
t.pendown()
t.forward(150)
t.left(90)
t.backward(250)
t.left(90)
t.forward(150)
t.left(90)
t.backward(250)

#draw pentagram
t.penup()
t.goto(-80,80)
t.pendown()
t.pencolor('red')
t.pensize(10)
t.forward(120)
t.left(144)
t.pencolor('yellow')
t.forward(120)
t.left(144)
t.pencolor('cyan')
t.forward(120)
t.left(144)
t.pencolor('green')
t.forward(120)
t.left(144)
t.pencolor('blue')
t.forward(120)
t.left(144)
#Draw N
t.left(90)
t.penup()
t.goto(-110,-150)
t.pendown()
t.right(180)
t.forward(150)
t.right(153)
t.forward(170)
t.left(153)
t.forward(150)
#Draw A
t.penup()
t.goto(-20,-150)
t.pendown()
t.right(18)
t.forward(160)
t.right(144)
t.forward(160)
t.right(-72)
t.penup()
t.goto(3,-80)
t.pendown()
t.forward(50)
#Draw H
t.penup()
t.goto(90,0)
t.pendown()
t.right(90)
t.forward(150)
t.penup()
t.goto(170,0)
t.pendown()
t.forward(150)
t.left(90)
t.penup()
t.goto(90,-80)
t.pendown()
t.forward(80)
#Draw L
t.penup()
t.goto(190,0)
t.pendown()
t.right(90)
t.forward(150)
t.left(90)
t.forward(80)
#Draw A
t.penup()
t.goto(280,-150)
t.pendown()
t.left(72)
t.forward(160)
t.right(144)
t.forward(160)
t.right(-72)
t.penup()
t.goto(303,-80)
t.pendown()
t.forward(50)