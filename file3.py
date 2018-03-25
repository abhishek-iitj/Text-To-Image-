import nltk
import numpy
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.tag import TrigramTagger
from nltk.corpus import treebank

train_data = treebank.tagged_sents()[:3000]
print train_data[0]
from nltk.tag import hmm

data=''
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


def ie_preprocess(data):
    trainer = hmm.HiddenMarkovModelTrainer()
    tagger = trainer.train_supervised(train_data)
    print tagger
    return tagger.tag(data.split())

sentence=ie_preprocess(data)

grammar = "NP: {<DT>?<JJ>*<NN>}"
grammar2="LEN: {<CD><IN>*<NN>}"
grammar3='''MES: {<NN><CD>|<CD><NN>|<\$><CD>|<CD><IN>*<NN>|<CC><CD>|<JJ><CD>}
            COLOR:{<JJ><NN>|<NN><JJ>|<NN><VBZ><JJ>}'''
chunked = []

cp = nltk.RegexpParser(grammar3)
for s in sentence:
    result=cp.parse(s)
    chunked.append(result)
    result.draw()