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
        myTurtle.circle(int(circleRadius))
        myTurtle.color(circleColor)
        myTurtle.end_fill()

