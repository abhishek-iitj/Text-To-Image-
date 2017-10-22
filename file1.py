#Tokenization and 2-gram model

from nltk import word_tokenize
from nltk.corpus import stopwords
from nltk import ngrams
import string
import configs
import turtle

def isMeasurment(x):
  # print x
  y=len(x)
  if(x[y-2]=='c' and x[y-1]=='m'):
    return True
  return False

objectList=[]       #an array of dictionary where each element will be a geometric shape

circleCount=0
rectangleCount=0
lineCount=0
triangleCount=0

with open('input.txt', 'r') as myfile:
    data=myfile.read().replace('\n', '')

print data

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




# myTurtle = turtle.Turtle()
# myTurtle.circle(50)
# turtle.getscreen()._root.mainloop()