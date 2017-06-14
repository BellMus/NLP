from nltk.tokenize import sent_tokenize,word_tokenize
from nltk.corpus import stopwords
import time

st=time.time()

txt="Hello python and numpy. How are you Mr. kapoor-rakshit? i am fine. What?"
sentences=sent_tokenize(txt)
print(sentences)
print()
words=word_tokenize(txt)
print(words)

filtered_sent=[]
stopwords_in_lang= set(stopwords.words("english"))
for i in words:
	if i not in stopwords_in_lang:
		filtered_sent.append(i)
print(stopwords_in_lang)
print(filtered_sent)

print(time.time()-st,"seconds")