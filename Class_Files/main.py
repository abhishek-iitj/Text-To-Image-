        #importing the required in-built and user-defined python files for the requirements
import turtle
import circle
import triangle
import rectangle

        #initialising variables for shapes
cirCle=0
recTangle=0
triAngle=0

fileCount=open("count.txt", 'r')
for line in fileCount:
    print line
    if 'rectangle' in line:
        recTangle=1
    if 'circle' in line:
        cirCle=1

#
# cirCle=1
# recTangle=1
# triAngle=0

        # Turtle Drawing variables of python in-built library
myTurtle = turtle.Turtle(shape="turtle")
myTurtle.hideturtle()

# myTurtle.penup()
# myTurtle.setposition(120,0)
# myTurtle.pendown()


            # if there is a circle in our text expression
if(cirCle>0):
    circleColor = ""    #initialising parameters as NULL
    circleRadius=0
    with open(circle.filePathCircle) as fpCircle:
        line = fpCircle.readline()
        cnt = 1
        while line:
            words=line.split()
            if(words[0]=="radius"):
                circleRadius=words[1]
            if(words[0]=="color"):
                circleColor=words[1]
            line = fpCircle.readline()
            cnt += 1
    for i in range(0,cirCle):
        Circle = circle.circle(circleColor, circleRadius)
        Circle.drawCircle()
                # if there is a rectangle in our text expression

print recTangle
if (recTangle > 0):
    rectangleLength = ""  # initialising parameters as NULL
    rectangleWidth = ""
    rectangleColor = ""
    with open(rectangle.filePathRectangle) as fpRectangle:
        line = fpRectangle.readline()
        cnt = 1
        while line:
            words = line.split()
            if (words[0] == "length"):
                rectangleLength = words[1]
            elif (words[0] == "width"):
                rectangleWidth = words[1]
            elif(words[0]=="color"):
                rectangleColor=words[1]
            line = fpRectangle.readline()
            cnt += 1
    print recTangle
    for i in range(0,recTangle):
        Rectangle = rectangle.rectangle(rectangleColor,rectangleLength,rectangleWidth)
        Rectangle.drawRectangle()



            #initial Testing for the turtle library
# myTurtle.penup()
# myTurtle.setposition(-1000, 0)
# myTurtle.pendown()
# myTurtle.circle(50)
#
# myTurtle.penup()
# myTurtle.setposition(60, 60)
# myTurtle.pendown()
# myTurtle.circle(50)
#
# myTurtle.penup()
# myTurtle.setposition(-60, 60)
# myTurtle.pendown()
# myTurtle.circle(50)
#
# myTurtle.penup()
# myTurtle.setposition(-180, 60)
# myTurtle.pendown()
# myTurtle.circle(50)



turtle.getscreen()._root.mainloop()
