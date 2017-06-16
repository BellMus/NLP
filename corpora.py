import nltk
from nltk.corpus import comparative_sentences
from nltk.tokenize import sent_tokenize


""" to track location of nltk_data directory.
 look for the data.py file here and here we will have location of our CORPORA :

 if sys.platform.startswith('win'):
    # Common locations on Windows:
    path += [
        str(r'C:\nltk_data'), str(r'D:\nltk_data'), str(r'E:\nltk_data'),
        os.path.join(sys.prefix, str('nltk_data')),
        os.path.join(sys.prefix, str('lib'), str('nltk_data')),
        os.path.join(os.environ.get(str('APPDATA'), str('C:\\')), str('nltk_data'))
    ]
else:
    # Common locations on UNIX & OS X:
    path += [
        str('/usr/share/nltk_data'),
        str('/usr/local/share/nltk_data'),
        str('/usr/lib/nltk_data'),
        str('/usr/local/lib/nltk_data')
    ]

    Example in windows it's generally : C:\Users\yourname\AppData\Roaming\nltk_data\corpora
"""
print(nltk.__file__)


sample=comparative_sentences.raw("labeledSentences.txt")              # checked from corpora folder
sent=sent_tokenize(sample)

print(sent[5])