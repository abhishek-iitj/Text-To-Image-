import turtle
myTurtle = turtle.Turtle(shape="turtle")
myTurtle.hideturtle()

filePathRectangle = 'rectangle.txt'
class rectangle(object):
                # Constructor for the rectangle
    def __init__(self,color,length,width):
        self.color=color
        self.length=length
        self.width=width
    def drawRectangle(self):
        myTurtle.begin_fill()
        myTurtle.color(self.color)
        myTurtle.forward(int(self.length))
        myTurtle.left(90)
        myTurtle.forward(int(self.width))
        myTurtle.left(90)
        myTurtle.forward(int(self.length))
        myTurtle.left(90)
        myTurtle.forward(int(self.width))
        myTurtle.end_fill()



