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
# default_tagger = nltk.data.load(nltk.tag._POS_TAGGER)

test_sent = brown.sents()[502]
# test_sent = [u'Noting', u'that', u'Plainfield', u'last', u'year', u'had', u'lost', u'the', u'Mack', u'Truck', u'Co.', u'plant', u',', u'he', u'said', u'industry', u'will', u'not', u'come', u'into', u'this', u'state', u'until', u'there', u'is', u'tax', u'reform', u'.']

def ie_preprocess(document):
    print document
    sentences = nltk.sent_tokenize(document)
    # print sentences
    trigram_tagger=nltk.TrigramTagger(brown_a, cutoff=0)
    sentences = [nltk.word_tokenize(sent) for sent in sentences]
    print "\nDefault tagger"
    x = [t0.tag(sent) for sent in sentences]
    print x
    print "\nUnigram tagger"
    x = [t1.tag(sent) for sent in sentences]
    print x
    print "\nBigram tagger"
    x = [t2.tag(sent) for sent in sentences]
    print x
    print "\nTrigram tagger"
    x = [t3.tag(sent) for sent in sentences]
    print x
    print "\n"
    # sentences = [nltk.pos_tag(sent) for sent in sentences
    trainer = hmm.HiddenMarkovModelTrainer()
    train_data = treebank.tagged_sents()[:3000]
    tagger = trainer.train_supervised(train_data)
    print tagger
    print "\nHMM tagger"
    x= [tagger.tag(sent) for sent in sentences]
    print x
    print "\nPOS Tag"
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