import nltk
import random
from nltk.corpus import movie_reviews
from nltk.tokenize import word_tokenize

def find_feature(document):
	words=set(document)
	features={}
	for w in word_features:
		features[w]=(w in words)
	return features

# train and test with this data. 
documents = [(list(movie_reviews.words(fileid)), category)
             for category in movie_reviews.categories()                  # one liner 
             for fileid in movie_reviews.fileids(category)]

#documents=[]
#for category in movie_reviews.categories():
#	for fileid in movie_reviews.fileids(category):
#		documents.append(list(movie_reviews.words(fileid),category))    # actually, a list with list of words 
                                                                        # and its category as pos, neg

"""print(documents)"""

random.shuffle(documents)       #  If we left them in order,chances are we'd train on all of the negatives, 
                                #  some positives, and then test only against positives. 

all_words = []                             # list of all words in database movie_reviews
for w in movie_reviews.words():
    all_words.append(w.lower())                

all_words = nltk.FreqDist(all_words)       # dictionary of frequency of words in a list

""" print(all_words.most_common(15)) """        # most commmon 15 words ie descending order of count 

""" print(all_words["rakshit"])"""              # count for a word -- "rakshit" it's me but result is 0

word_features=[]                             # get words which will act as feature, find in our positive and negative documents, 
                                             # marking their presence as either true or false.

for k,v in all_words.most_common(3000): 
	word_features.append(k.encode("utf-8"))  # to remove u' used encoding format

"""print(word_features)"""
"""print(find_feature(movie_reviews.words('neg/cv000_29416.txt')))"""  # testing on one of featuresets

""" Do same for entire  all of our documents, 
 saving the feature existence booleans and their respective positive or negative categories as:"""

featuresets = [(find_feature(rev), category) for (rev, category) in documents]

"""This is called supervised machine learning, because we're showing the machine data, 
and telling it "hey, this data is positive," or "this data is negative." 
Then, after that training is done, we show the machine some new data and ask the computer, based on what we taught the computer before, 
what the computer thinks the category of the new data is."""

trainingset=featuresets[:1900]
testingset=featuresets[1900:]

classifier = nltk.NaiveBayesClassifier.train(trainingset)

"""If it guesses correctly what we know the answer to be, then the computer got it right.
 varying accuracy, but you should see something from 60-75% on average."""

print("Classifier accuracy percent:",(nltk.classify.accuracy(classifier, testingset))*100)

"""What this tells you is the ratio of occurences in negative to positive, or visa versa, for every word. 
So here, we can see that the term "insulting" appears 10.6 more times as often in negative reviews as it does in positive reviews. Ludicrous, 10.1."""

classifier.show_most_informative_features(15)