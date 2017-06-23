# NLP
Practice and examples of using nltk library for NLP
<br>
<ul>
<li><b>Tokenization</b><br>
Splitting sentences (sentence tokenizer) and words (word tokenizer) from the body of text.
<li><b>StopWords</b><br>
Words that are useless, and we wish to do nothing with them. So they are removed from text. 
<li><b>Stemming</b><br>
Normalization, in terms of affixes involved with words.<br>
Example : riding === ride , normalization with -ing affix.<br>
Algorithms involved in stemming are <b>PorterStemmer</b>, <b>LancasterStemmer</b>, <b>SnowballStemmer</b>
<li><b>Lemmatizing</b><br>
Similar to stemming, Stemming can often create non-existent words, whereas lemmas are actual words.<br>
Stemmed word may not be something you can just look up in a dictionary, but you can look up a lemma.
<li><b>POS - Part Of Speech tagging</b><br>
Labeling words in a sentence as nouns, adjectives, verbs...etc. along with tense forms.<br>
For complete list of POS tags refer to <b>nlpfile.py</b> above.
<li><b>NER - Named Entity Recognition</b><br>
Pull out entities like people, places, things, locations, monetary figures etc.
<li><b>Chunking<b/><br>
To group the words in text based on Nouns(generally), verbs etc. , to have an idea what the sentence is about.
<li><b>Chinking<b/><br>
Chunk without the Chink, ie to group except certain parts of speech.
</ul>
