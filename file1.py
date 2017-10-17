from nltk import word_tokenize
from nltk.corpus import stopwords
from nltk import ngrams
import string
import configs.py
import turtle

def isMeasurment(x):
  y=len(x)
  if(x[y-1]=='c' and x[y-2]=='m'):
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
  print  type(twograms)
  for grams in twograms:
    # print grams
    list(grams)
    # if(isMeasurment(grams[1])==True):



  stop = stopwords.words('english') + list(string.punctuation)
  temp= [i for i in word_tokenize(ary[i].lower()) if i not in stop]



# myTurtle = turtle.Turtle()
# myTurtle.circle(50)
# turtle.getscreen()._root.mainloop()