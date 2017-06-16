""" SOURCE : https://pythonprogramming.net/"""

import nltk
from nltk.tokenize import sent_tokenize,word_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer, LancasterStemmer, SnowballStemmer, WordNetLemmatizer

import time

st=time.time()

txt="Hello pypy numpy. How are you Mr. kapoor-rakshit? Pythoning? and guessing, What? Going google Pyers developers riding   a car."

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

tagged=nltk.pos_tag(words)                            # part of speech tagging over a list of words
print(*tagged,sep="\n")


chunkregex=r"""chunk: {<RB.?>*<VB.?>*<NNP>+<NN>?}"""
chunkparser=nltk.RegexpParser(chunkregex)
chunked=chunkparser.parse(tagged)                                 # NLTK tree variable (chunked)
print(chunked)

for i in chunked.subtrees(filter=lambda t:t.label()=="chunk"):    # iterate the tree using .subtrees()
	print(i)                                                      # print only chunked parts of tree

"""chunked.draw()"""                                                   # GUI interface  

"""The idea here is to group nouns with the words that are in relation to them.

<RB.?>* = "0 or more of any tense of adverb, RB;RBR;RBS as max. length can be 3, and all such occurrences" followed by:

<VB.?>* = "0 or more of any tense of verb," followed by:

<NNP>+ = "One or more proper nouns," followed by

<NN>? = "zero or one singular noun.

'.' = matches any character except a newline

'*' = match 0 or more repetitions of the preceding RE. ex:- ab* will match ‘a’, ‘ab’, or ‘a’ followed by any number of ‘b’s.

'?' = match 0 or 1 (ie OFF or ON)repetitions of the preceding RE. ab? will match either ‘a’ or ‘ab’.

'+' = match 1 or more repetitions of the preceding RE. ab+ will match ‘a’ followed by any non-zero number of ‘b’s; it will not match just ‘a’."""


"""Chunk everything except }----here----{"""
chinkregex=r"""chink: {<.*>+}                            #important in next line, the chink part   
                      }<VB.?|IN|DT|TO>+{"""              #we're removing from the chink one or more verbs, prepositions, determiners, or the word 'to'.
chinkparser=nltk.RegexpParser(chinkregex)
chinked=chinkparser.parse(tagged)
print(chinked)


namedentity=nltk.ne_chunk(tagged,binary=True)           # Named entity recognition
print(namedentity)
"""namedentity.draw()"""

""" named entity to describe the word in detail (binary=False) and no detail ie just NE recognised (binary=True)

ORGANIZATION - Georgia-Pacific Corp., WHO
PERSON - Eddy Bonte, President Obama
LOCATION - Murray River, Mount Everest
DATE - June, 2008-06-29
TIME - two fifty a m, 1:30 p.m.
MONEY - 175 million Canadian Dollars, GBP 10.40
PERCENT - twenty pct, 18.75 %
FACILITY - Washington Monument, Stonehenge
GPE - South East Asia, Midlothian"""


""" stemming can often create non-existent words, whereas lemmas are actual words. 
Some times you will wind up with a very similar word, but sometimes, you will wind up with a completely different word.
lemmatize takes a part of speech parameter, "pos=v, pos=a." If not supplied, the default is "noun." 
This means that an attempt will be made to find the closest noun, which can create trouble for you. """

wnlm=WordNetLemmatizer()
for i in words:
	print(wnlm.lemmatize(i,pos="v"))

print(time.time()-st,"seconds")