        #importing the required in-built and user-defined python files for the requirements
import turtle
import circle
import triangle
import rectangle
import math

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


# READING PLACEMENT FILE INPUTS ACCORDINGLY

filePlacement = open("placement.txt", 'r')
line_placement = filePlacement.readline()
words_placement=line_placement.split()

print len(words_placement)

first=words_placement[0]
print first
position_distance=int(words_placement[1])
print position_distance

second=words_placement[len(words_placement)-1]
print second
if(len(words_placement)==4):
    position_direction=words_placement[2];
else:
    position_direction = words_placement[2]+words_placement[3];
print position_direction



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

if(first=="circle" and second=="rectangle"):
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
            Circle = circle.circle(circleColor, circleRadius,0,0)
            Circle.drawCircle()
                    # if there is a rectangle in our text expression

    print 1
    # myTurtle.penup()
    # myTurtle.setposition(0,-50)
    # myTurtle.pendown()
    print 2
    # print recTangle

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
            if(position_direction=="bottomleft"):
                x=-math.sqrt(position_distance*position_distance/2)
                y=x
            if (position_direction == "bottomright"):
                x = math.sqrt(position_distance*position_distance/ 2)
                y = -x
            if (position_direction == "topleft"):
                x = -math.sqrt(position_distance*position_distance / 2)
                y = -x
            if (position_direction == "topright"):
                x = math.sqrt(position_distance*position_distance / 2)
                y = x
            if (position_direction == "top"):
                x = 0 #math.sqrt(position_distance / 2)
                y = position_distance

            if (position_direction == "bottom"):
                x = 0#-math.sqrt(position_distance / 2)
                y = -position_distance

            if (position_direction == "left"):
                x = -position_distance #math.sqrt(position_distance / 2)
                y = 0
            if (position_direction == "right"):
                x = position_distance#-math.sqrt(position_distance / 2)
                y = 0

            print x,y
            Rectangle = rectangle.rectangle(rectangleColor,rectangleLength,rectangleWidth,x,y)
            Rectangle.drawRectangle()

else:
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
                elif (words[0] == "color"):
                    rectangleColor = words[1]
                line = fpRectangle.readline()
                cnt += 1
        print recTangle
        for i in range(0, recTangle):
            Rectangle = rectangle.rectangle(rectangleColor, rectangleLength, rectangleWidth,0,0)
            Rectangle.drawRectangle()

    if (cirCle > 0):
        circleColor = ""  # initialising parameters as NULL
        circleRadius = 0

        with open(circle.filePathCircle) as fpCircle:
            line = fpCircle.readline()
            cnt = 1
            while line:
                words = line.split()
                if (words[0] == "radius"):
                    circleRadius = words[1]
                if (words[0] == "color"):
                    circleColor = words[1]
                line = fpCircle.readline()
                cnt += 1
        for i in range(0, cirCle):
            if (position_direction == "bottomleft"):
                x = -math.sqrt(position_distance * position_distance / 2)
                y = x
            if (position_direction == "bottomright"):
                x = math.sqrt(position_distance * position_distance / 2)
                y = -x
            if (position_direction == "topleft"):
                x = -math.sqrt(position_distance * position_distance / 2)
                y = -x
            if (position_direction == "topright"):
                x = math.sqrt(position_distance * position_distance / 2)
                y = x
            if (position_direction == "top"):
                x = 0  # math.sqrt(position_distance / 2)
                y = position_distance

            if (position_direction == "bottom"):
                x = 0  # -math.sqrt(position_distance / 2)
                y = -position_distance

            if (position_direction == "left"):
                x = -position_distance  # math.sqrt(position_distance / 2)
                y = 0
            if (position_direction == "right"):
                x = position_distance  # -math.sqrt(position_distance / 2)
                y = 0

            print x, y
            Circle = circle.circle(circleColor, circleRadius,x,y)
            Circle.drawCircle()
            # if there is a rectangle in our text expression

turtle.getscreen()._root.mainloop()
