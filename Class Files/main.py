import turtle

myTurtle = turtle.Turtle(shape="turtle")
# myTurtle.penup()
# myTurtle.setposition(120,0)
# myTurtle.pendown()
myTurtle.circle(50)

myTurtle.penup()
myTurtle.setposition(-1000, 0)
myTurtle.pendown()
myTurtle.circle(50)

myTurtle.penup()
myTurtle.setposition(60, 60)
myTurtle.pendown()
myTurtle.circle(50)

myTurtle.penup()
myTurtle.setposition(-60, 60)
myTurtle.pendown()
myTurtle.circle(50)
#
# myTurtle.penup()
# myTurtle.setposition(-180, 60)
# myTurtle.pendown()
# myTurtle.circle(50)

turtle.getscreen()._root.mainloop()