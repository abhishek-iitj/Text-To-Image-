import turtle
myTurtle = turtle.Turtle(shape="turtle")
myTurtle.hideturtle()

filePathCircle = 'circle.txt'
class circle(object):
                    # Constructor for the circle
    def __init__(self,color,radius,x,y):
        self.color=color
        self.radius=radius
        self.posX=x
        self.posY=y

    def drawCircle(self):
        myTurtle.penup()
        myTurtle.setposition(self.posX, self.posY)
        myTurtle.pendown()

        myTurtle.penup()
        myTurtle.setposition(self.posX, self.posY-int(self.radius))
        myTurtle.pendown()


        myTurtle.begin_fill()
        myTurtle.circle(int(self.radius))
        myTurtle.color(self.color)

        myTurtle.end_fill()

        myTurtle.penup()
        myTurtle.setposition(self.posX, self.posY+int(self.radius))
        myTurtle.pendown()
