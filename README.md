# Text-To-Image-
## BTP CS 398 + 399 : 
An application which takes as input a description of a scene in natural language and produces an image or scene giving a gist of that description. 

### Example Input : 
Draw a rectangle of 100cm length and 50cm width and its color is green. there is a circle of blue color and its radius is 50cm. the circle is 200cm top of rectangle.

### Output: [Click Here](https://drive.google.com/file/d/1ET-NEm3_8T4NQtcEwrQ-0ocTo9rLQtEU/view?usp=sharing).

### Prerequisite:

  1. Python 2.7
  
  2. Python NLTK Library [Installation](https://www.nltk.org/install.html)
  
     -Run these commands in a python shell to get all the packages from NLTK
    
    ```import nltk```
    ```nltk.download('all')``` (Takes approx 20-30 minutes)
    
  3. Python Turtle Library 
  
  4. PyCharm IDE (Preferred)

### How to Run the project:

  1. ```git clone https://github.com/abhishek-iitj/Text-To-Image-.git```
  2. ```cd Text-To-Image```
  
  3. Write the input text in "input.txt" (following the assumptions) (Read the assumptions here)
  
  4. Follow these steps to see outputs of following algorithms
  
  
#### Algorithm 1: String Matching

   - It will generate an image for the input text.

   - Run the files ```phase2.py``` first and then ```Class_Files/main1.py```
    
   - All the next algorithms will generate the intermediate results as the output and not the image. 
 
 #### Algorithm 2: POS Chunking(Without context):
 
   - It will generate the chunks as per the grammar rules defined in the file ```file2.py```
  
   - Run the file ```file2.py```
 
 #### Algorithm 3: POS Chunking(With context):
 
   - It will generate the chunks as per the NLTK default taggers taking context into consideration.
  
   - Run the file ```tagger.py```
      
 #### Algorithm 4: (Algorithm 2 + Algorithm 1):
 
   - It will generate the chunks as per the string matching on top of the output of NLTK POS_TAG function as per the grammar rules defined in the file ```file4.py```
  
   - Run the file ```file4.py```
 
   - You can see the correct chunks of COL{Color}, MES{Measurements} and SHAPE{Shapes}. 
   
   
 Some of the ouptuts in visual form can be found here. 
