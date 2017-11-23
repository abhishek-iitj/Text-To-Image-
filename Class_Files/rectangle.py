import turtle
myTurtle = turtle.Turtle(shape="turtle")
myTurtle.hideturtle()

filePathRectangle = 'rectangle.txt'
class rectangle(object):
                # Constructor for the rectangle
    def __init__(self,color,length,width,x,y):
        self.color=color
        self.length=length
        self.width=width
        self.posX=x
        self.posY=y
    def drawRectangle(self):
        myTurtle.penup()
        myTurtle.setposition(self.posX,self.posY)
        myTurtle.pendown()

        myTurtle.penup()
        myTurtle.setposition(self.posX, self.posY+int(self.width)/2)
        myTurtle.pendown()

        myTurtle.begin_fill()
        myTurtle.color(self.color)
        myTurtle.forward(int(int(self.length)/2))
        myTurtle.right(90)

        myTurtle.forward(int(self.width))
        myTurtle.right(90)

        myTurtle.forward(int(self.length))
        myTurtle.right(90)

        myTurtle.forward(int(self.width))
        myTurtle.right(90)

        myTurtle.forward(int(int(self.length )/ 2))
        myTurtle.right(90)
        myTurtle.end_fill()

        myTurtle.penup()
        myTurtle.setposition(self.posX, self.posY -int(self.width)/ 2)
        myTurtle.pendown()





