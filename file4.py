import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
def ie_preprocess(document):
    sentences = nltk.sent_tokenize(document)
    # print sentences
    sentences = [nltk.word_tokenize(sent) for sent in sentences]
    # print 1
    # print sentences
    model = {'color': 'COLOR', 'length':'MES', 'width':'MES', 'radius':'MES'}
    sentences = [nltk.pos_tag(sent) for sent in sentences]
    # print sentences
    return sentences

data=''
originaldata=''
with open('input.txt', 'r') as myfile:
    data=myfile.read().replace('\n', '')
    stop_words = set(stopwords.words('english'))
    word_tokens = word_tokenize(data)
    filtered_sentence = [w for w in word_tokens if not w in stop_words]
    print filtered_sentence
    data=""
    for i in range(0, len(filtered_sentence)):
        data=data+" "+filtered_sentence[i]
    print data
    originaldata=""
    for word in data.split():
        if word=='circle' or word=='rectangle':
            word=''
        else:
            originaldata+=word+" "
    print originaldata

sentence=ie_preprocess(data)
print(sentence)
sentence=list(sentence)
print sentence[0][0][1]

n=100
mylist=[[[0 for _ in range(2)] for _ in range(n)] for _ in range(1)]
mylist=[]
print(len(sentence))
print(len(sentence[0]))

for i in range(0, len(sentence)):
    temp=[]
    for j in range(0, len(sentence[i])):
        temp2=[]
        temp2.append(sentence[i][j][0])
        temp2.append(sentence[i][j][1])
        if(sentence[i][j][0]=='color'):
            # print(sentence[i][j])
            temp2[1]='COLOR'
        elif(sentence[i][j][0]=='radius'):
            temp2[1] = 'MES'
        elif (sentence[i][j][0] == 'length'):
            temp2[1] = 'MES'
        elif (sentence[i][j][0] == 'width'):
            temp2[1] = 'MES'
        elif(sentence[i][j][0] == 'circle' or sentence[i][j][0]=='rectangle'):
            temp2[1] = 'SHAPE'
        temp.append(tuple(temp2))
    mylist.append(temp)

print(mylist)
# sentence=[[('Draw', 'NNP'), ('green', 'JJ'), ('color', 'COLOR'), ('100cm', 'CD'), ('radius', 'MES'), ('.', '.')], [('A', 'DT'), ('color', 'COLOR'), ('blue', 'JJ'), ('dimensions', 'NNS'), ('300cm', 'CD'), ('length', 'MES'), ('width', 'MES'), ('200cm', 'CD'), ('.', '.')], [('The', 'DT'), ('50cm', 'CD'), ('bottom-left', 'NN'), ('.', '.')]]
grammar = "NP: {<DT>?<JJ>*<NN>}"
grammar2="LEN: {<CD><IN>*<NN>}"
grammar3='''MES: {<MES><CD>|<CD><MES>}
            SHAPE: {<SHAPE>}
            COLOR:{<JJ><COLOR>|<COLOR><JJ>}'''
chunked = []

cp = nltk.RegexpParser(grammar3)
for s in mylist:
    result=cp.parse(s)
    chunked.append(result)
    result.draw()
