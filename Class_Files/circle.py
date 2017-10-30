import turtle
myTurtle = turtle.Turtle(shape="turtle")
myTurtle.hideturtle()

filePathCircle = 'circle.txt'
class circle(object):
                    # Constructor for the circle
    def __init__(self,color,radius):
        self.color=color
        self.radius=radius


    def drawCircle(Self):
        myTurtle.begin_fill()
        myTurtle.circle(int(Self.radius))
        myTurtle.color(Self.color)
        myTurtle.end_fill()

