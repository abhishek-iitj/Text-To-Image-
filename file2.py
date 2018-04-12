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
    print sentences
    return sentences

data=''
originaldata=''
with open('input6.txt', 'r') as myfile:
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
i


sentence=ie_preprocess(originaldata)
#sentence = [("the", "DT"), ("little", "JJ"), ("yellow", "JJ"), ("dog", "NN"), ("barked", "VBD"), ("at", "IN"), ("the", "DT"), ("cat", "NN")]
grammar = "NP: {<DT>?<JJ>*<NN>}"
grammar2="LEN: {<CD><IN>*<NN>}"
grammar3='''MES: {<NN><CD>|<CD><NN>|<\$><CD>|<CD><IN>*<NN>|<CC><CD>|<JJ><CD>|<CD><JJ>|<VBZ><CD>|<VBP><CD>}
            COLOR:{<NN><NN>|<JJ><NN>|<NN><JJ>|<NN><VBZ><JJ>}'''
chunked = []

cp = nltk.RegexpParser(grammar3)
for s in sentence:
    result=cp.parse(s)
    chunked.append(result)
    result.draw()
# print chunked
