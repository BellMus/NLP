from nltk.corpus import wordnet

syns=wordnet.synsets("innocent")

print(syns)                        # a list of Synsets with part of speech, eg:- Synset(good.n.01) first noun
print(syns[1].lemmas())            # [Lemma('good.n.02.good'), Lemma('good.n.02.goodness')]


for i in syns:
	print(i.name())                            # good.n.01

	for l in i.lemmas():                       # synonyms list
		print("synonym : ",l.name())           # synonyms    eg:- good, goodness

		if l.antonyms():                       
			k=l.antonyms()                     # antonym list 
			for j in k:
				print("antonym : ",j.name())   # antonym

	print(i.definition())                      # definition

	print(i.examples())                        # example usage
	print("\n")


w1=wordnet.synset("computer.n.01")
w2=wordnet.synset("pc.n.01")
print(w1.wup_similarity(w2))                   # generates semantic similarity between two words
