import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.corpus import treebank
from nltk.tag import hmm
from nltk import DefaultTagger, UnigramTagger, BigramTagger, TrigramTagger
from nltk.corpus import brown
brown_a =nltk.corpus.brown.tagged_sents(categories=['news', 'editorial', 'reviews'])
text = brown.tagged_sents(categories='news')[:500]

t0 = DefaultTagger('NN')
t1 = UnigramTagger(text, backoff=t0)
t2 = BigramTagger(text, backoff=t1)
t3 = TrigramTagger(text, backoff=t1)

test_sent = brown.sents()[502]
# test_sent = [u'Noting', u'that', u'Plainfield', u'last', u'year', u'had', u'lost', u'the', u'Mack', u'Truck', u'Co.', u'plant', u',', u'he', u'said', u'industry', u'will', u'not', u'come', u'into', u'this', u'state', u'until', u'there', u'is', u'tax', u'reform', u'.']

def ie_preprocess(document):
    print document
    sentences = nltk.sent_tokenize(document)
    # print sentences
    trigram_tagger=nltk.TrigramTagger(brown_a, cutoff=0)
    sentences = [nltk.word_tokenize(sent) for sent in sentences]
    print "Default tagger\n"
    x = [t0.tag(sent) for sent in sentences]
    print x
    print "Unigram tagger\n"
    x = [t1.tag(sent) for sent in sentences]
    print x
    print "Bigram tagger\n"
    x = [t2.tag(sent) for sent in sentences]
    print x
    print "Trigram tagger\n"
    x = [t3.tag(sent) for sent in sentences]
    print x
    # sentences = [nltk.pos_tag(sent) for sent in sentences
    trainer = hmm.HiddenMarkovModelTrainer()
    train_data = treebank.tagged_sents()[:3000]
    tagger = trainer.train_supervised(train_data)
    print tagger
    print "HMM tagger\n"
    x= [tagger.tag(sent) for sent in sentences]
    print x
    print "POS Tag\n"
    sentences = [nltk.pos_tag(sent) for sent in sentences]
    print sentences
    return sentences

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


sentence=ie_preprocess(data)
# print sentence
#sentence = [("the", "DT"), ("little", "JJ"), ("yellow", "JJ"), ("dog", "NN"), ("barked", "VBD"), ("at", "IN"), ("the", "DT"), ("cat", "NN")]
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
print chunked
