from nltk.tokenize import sent_tokenize,word_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
import time

st=time.time()

txt="Hello python and numpy. How are you Mr. kapoor-rakshit? .And guessing, What? Going google Pyers developers riding   a car."

sentences=sent_tokenize(txt)                            # separate sentences
print(sentences)
print()
words=word_tokenize(txt)                                # separate words
print(*words,sep="\n")


filtered_sent=[]
stopwords_in_lang= set(stopwords.words("english"))     # set of words in "english" language which are not required for analysis like "and, is" 
for i in words:
	if i not in stopwords_in_lang:
		filtered_sent.append(i)
#print(stopwords_in_lang)                             # print stopwords in "english"
print(filtered_sent)                                  # words without stopwords


ps=PorterStemmer()                                    # porterstemmer algo for stemming
for w in words:
	print(ps.stem(w))                                 # apply algo on each word

print(time.time()-st,"seconds")