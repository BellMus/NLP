import nltk
from nltk.tokenize import sent_tokenize,word_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer, LancasterStemmer, SnowballStemmer

import time

st=time.time()

txt="Hello python and numpy. How are you Mr. kapoor-rakshit? .and guessing, What? Going google Pyers developers riding   a car."

sentences=sent_tokenize(txt)                            # separate sentences
print(sentences)
print()
words=word_tokenize(txt)                                # separate words
print(*words)



filtered_words=[]
stopwords_in_lang= set(stopwords.words("english"))     # set of words in "english" language which are not required for analysis like "and, is" 
for i in words:
	if i not in stopwords_in_lang:
		filtered_words.append(i)
#print(stopwords_in_lang)                             # print stopwords in "english"
print(filtered_words)                                 # words without stopwords



"""SOURCE CODE for PorterStemmer @ https://tartarus.org/martin/PorterStemmer/python.txt"""

ps=PorterStemmer()                                    # porterstemmer algo for stemming
ls=LancasterStemmer()                                 # lancasterstemmer algo for stemming
ss=SnowballStemmer("english")                         # snowballstemmer algo for stemming
pslist=[]
lslist=[]
sslist=[]
for w in words:
	pslist.append(ps.stem(w))                                 # apply algo on each word
	lslist.append(ls.stem(w))
	sslist.append(ss.stem(w))
print(*pslist)
print(*lslist)
print(*sslist)


"""POS tag list:

CC	coordinating conjunction
CD	cardinal digit
DT	determiner
EX	existential there (like: "there is" ... think of it like "there exists")
FW	foreign word
IN	preposition/subordinating conjunction
JJ	adjective	'big'
JJR	adjective, comparative	'bigger'
JJS	adjective, superlative	'biggest'
LS	list marker	1)
MD	modal	could, will
NN	noun, singular 'desk'
NNS	noun plural	'desks'
NNP	proper noun, singular	'Harrison'
NNPS	proper noun, plural	'Americans'
PDT	predeterminer	'all the kids'
POS	possessive ending	parent's
PRP	personal pronoun	I, he, she
PRP$	possessive pronoun	my, his, hers
RB	adverb	very, silently,
RBR	adverb, comparative	better
RBS	adverb, superlative	best
RP	particle	give up
TO	to	go 'to' the store.
UH	interjection	errrrrrrrm
VB	verb, base form	take
VBD	verb, past tense	took
VBG	verb, gerund/present participle	taking
VBN	verb, past participle	taken
VBP	verb, sing. present, non-3d	take
VBZ	verb, 3rd person sing. present	takes
WDT	wh-determiner	which
WP	wh-pronoun	who, what
WP$	possessive wh-pronoun	whose
WRB	wh-abverb	where, when"""

print(nltk.pos_tag(words))                            # part of speech tagging over a list of words

print(time.time()-st,"seconds")