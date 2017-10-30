#Tokenization and 2-gram model
# assuming each sentence contains only one type of shape
from nltk import word_tokenize
from nltk.corpus import stopwords
from nltk import ngrams
import re
import string
import configs
import turtle
import os
print configs.color

fileCircle = open('Class_Files/circle.txt', 'w')
fileRectangle = open('Class_Files/rectangle.txt', 'w')
fileCount=open('Class_Files/count.txt', 'w')

def getNumber(x):
  return x[:-2]
def isMeasurment(x):
  # print x
  y=len(x)
  if(x[y-2]=='c' and x[y-1]=='m'):
    return True
  return False
def isColor(x):
  if x in configs.color:
    return True
  return False

objectList=[]       #an array of dictionary where each element will be a geometric shape

circleCount=0
rectangleCount=0
lineCount=0
triangleCount=0

with open('input4.txt', 'r') as myfile:
    data=myfile.read().replace('\n', '')

data=data.lower()
print data

circleAttributes={}
rectangleAttributes={}

ary=[sentence + '.' for sentence in data.split('.')]
for i in range(len(ary)):
  n = 2
  twograms = ngrams(ary[i].split(), n)
  # print  type(twograms)
  for grams in twograms:
    # print grams
    list(grams)
    if(isMeasurment(grams[1])==True):
      # print grams[1]
      if(grams[0]=='radius'):
        circleCount+=1

      elif (grams[0] == 'length' or grams[0]=='width'):
        rectangleCount+= 0.5
  stop = stopwords.words('english') + list(string.punctuation)
  temp= [i for i in word_tokenize(ary[i].lower()) if i not in stop]

print "No. of Circles", circleCount

print "No. of Rectangle", rectangleCount

for i in range(len(ary)):
  wordList = re.sub("[^\w]", " ", ary[i]).split()
  circle=0
  rectangle=0
  triangle=0
  square=0          #for each sentence we try to find which shape is being talked about
  print "Under Inspection : ", wordList
  for j in range(len(wordList)):
    if(wordList[j]=='circle'):
      circle=1
      break
    elif (wordList[j]=='rectangle'):
      rectangle=1
      break
    elif (wordList[j]=='triangle'):
      triangle=1
      break
    elif (wordList[j]=='square'):
      square=1
      break

  if(circle==1):    #try to find radius and color in that sentence
    circleCount=1
    print "     Found Circle"
    radius=0
    radiusIndex=-1
    color=0
    colorIndex=-1
    for j in range(len(wordList)):    #try to find occurence of the words 'radius' and 'color'
      if (wordList[j] == 'radius'):
        radius=1
        radiusIndex=j
      if (wordList[j]=='color'):
        color=1
        colorIndex=j
        print "Color found at index ", j
    if(radius==1):                              #search for the length in the vicinity of radius
      flagR=0       #Radius Flag
      for x in range(radiusIndex, len(wordList)):     #search for the right length in the vicinity of radius
        if(isMeasurment(wordList[x])):
          circleAttributes['radius']=wordList[x]
          flagR=1
          print "circle radius is ", wordList[x]
          temp=getNumber(wordList[x])
          fileCircle.write("radius "+(temp)+"\n")
          break

      if (flagR==0):    #not found in right
        for x in range(radiusIndex, 0, -1):               #search for the right length in the vicinity of radius
          if (isMeasurment(wordList[x])):
            circleAttributes['radius'] = wordList[x]
            print "circle radius is ", wordList[x]
            fileCircle.write("radius " + (temp) + "\n")
            break

    if (color == 1):                  # search for a colorWord in the vicinity of color
      flagC=0           #Color Flag
      for x in range(colorIndex, 0, -1):
        if (isColor(wordList[x])):
          circleAttributes['color'] = wordList[x]
          flagC=1
          print "circle color is ", wordList[x]
          fileCircle.write("color " + (wordList[x]) + "\n")

      if (flagC == 0):  # not found in left
        for x in range(colorIndex, len(wordList)):  # search for the colorWord in right the vicinity of color
          if (isColor(wordList[x])):
            circleAttributes['color'] = wordList[x]
            print "circle radius is ", wordList[x]
            fileCircle.write("color " + (wordList[x]) + "\n")
            break

  if (rectangle== 1):  # try to find radius and color in that sentence
    rectangleCount=1
    print "     Found Rectangle"
    length = 0
    lengthIndex = -1
    width = 0
    widthIndex = -1
    color = 0
    colorIndex = -1
    for j in range(len(wordList)):  # try to find occurence of the words 'length' and 'width' and 'color'
      if (wordList[j] == 'length'):
        length = 1
        lengthIndex = j
      if (wordList[j] == 'width'):
        width = 1
        widthIndex = j
      if (wordList[j] == 'color'):
        color = 1
        colorIndex = j

    if (length == 1):  # search for the number in the vicinity of length
      flagL = 0  # Length Flag
      for x in range(lengthIndex, len(wordList)):  # search for the number in the right vicinity of width
        if (isMeasurment(wordList[x])):
          rectangleAttributes['length'] = wordList[x]
          flagL = 1
          print "Rectangle Length is ", wordList[x]
          temp = getNumber(wordList[x])
          fileRectangle.write("length " + (temp) + "\n")
          break

      if (flagL == 0):  # not found in right
        for x in range(lengthIndex, 0, -1):             # search for the number in the left vicinity of length
          if (isMeasurment(wordList[x])):
            rectangleAttributes['length'] = wordList[x]
            print "Rectangle Length is ", wordList[x]
            temp = getNumber(wordList[x])
            fileRectangle.write("length " + (temp) + "\n")
            break

    if (width == 1):     # search for the number in the vicinity of width
      flagW = 0  # Width Flag
      for x in range(widthIndex, len(wordList)):  # search for the number in the right vicinity of width
        if (isMeasurment(wordList[x])):
          rectangleAttributes['width'] = wordList[x]
          flagW = 1
          print "Rectangle Width is ", wordList[x]
          temp = getNumber(wordList[x])
          fileRectangle.write("width " + (temp) + "\n")
          break

      if (flagW == 0):  # not found in right
        for x in range(widthIndex, 0, -1):  # search for the number in the left vicinity of width
          if (isMeasurment(wordList[x])):
            rectangleAttributes['width'] = wordList[x]
            print "Rectangle Width is ", wordList[x]
            temp = getNumber(wordList[x])
            fileRectangle.write("width " + (temp) + "\n")
            break

    if (color == 1):  # search for a colorWord in the vicinity of color
      flagC = 0  # Color Flag
      for x in range(colorIndex, 0, -1):
        if (isColor(wordList[x])):
          rectangleAttributes['color'] = wordList[x]
          flagC = 1
          print "Rectangle color is ", wordList[x]
          fileRectangle.write("color " + wordList[x] + "\n")

      if (flagC == 0):  # not found in left
        for x in range(colorIndex, len(wordList)):  # search for the colorWord in right the vicinity of color
          if (isColor(wordList[x])):
            rectangleAttributes['color'] = wordList[x]
            print "Rectangle color is ", wordList[x]
            fileRectangle.write("color " + wordList[x] + "\n")

if(circleCount>0):
  fileCount.write('circle '+str(circleCount)+"\n")
if(int(rectangleCount)>0):
  fileCount.write('rectangle ' + str(int(rectangleCount))+"\n")

# os.system('python Class_Files/main.py')