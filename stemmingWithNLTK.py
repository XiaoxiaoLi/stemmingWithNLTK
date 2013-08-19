#use different stemmers and lemmatizers provided by NLTK

#see http://nltk.org/api/nltk.stem.html for full NLTK stemmer module documentations

#to use the WordNet Lemmatizer
from nltk.corpus import wordnet as wn
from nltk.stem.wordnet import WordNetLemmatizer #To download corpora: python -m nltk.downloader all
lmtzr=WordNetLemmatizer()#create a lemmatizer object

#to use Porter stemmer
from nltk.stem.porter import PorterStemmer
porterStemmer = PorterStemmer()

#to the snowball stemmer
from nltk.stem.snowball import EnglishStemmer
snowBallStemmer = EnglishStemmer()

#to use the Lancaster stemmer
from nltk.stem.lancaster import LancasterStemmer
lanStemmer = LancasterStemmer()

term = 'cats'
print term
print 'WordNet Lemmatizer: ' + lmtzr.lemmatize(term)
print 'Porter Stemmer: ' + porterStemmer.stem(term)
print 'SnowBall Stemmer: '+ snowBallStemmer.stem(term)
print 'Lancaster Stemmer: '+ lanStemmer.stem(term)