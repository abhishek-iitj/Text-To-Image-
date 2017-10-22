import nltk
def ie_preprocess(document):
    sentences = nltk.sent_tokenize(document)
    print sentences
    sentences = [nltk.word_tokenize(sent) for sent in sentences]
    print sentences
    sentences = [nltk.pos_tag(sent) for sent in sentences]
    print sentences
    return sentences

data=''
with open('input.txt', 'r') as myfile:
    data=myfile.read().replace('\n', '')

sentence=ie_preprocess(data)
#sentence = [("the", "DT"), ("little", "JJ"), ("yellow", "JJ"), ("dog", "NN"), ("barked", "VBD"), ("at", "IN"), ("the", "DT"), ("cat", "NN")]
grammar = "NP: {<DT>?<JJ>*<NN>}"
grammar2="LEN: {<$><CD>}"
chunked = []

cp = nltk.RegexpParser(grammar2)
for s in sentence:
    result=cp.parse(s)
    chunked.append(result)
    result.draw()
print chunked