from nltk.tokenize import sent_tokenize
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer



# Get the text
text = "Some text from main file"

# sentence-tokenized copy of text
sentences = sent_tokenize(text)

sentences_num = len(sentences)

ps = PorterStemmer()

def text_to_words(sentences):
    """
    Process the sentences in text to a list of stemmed words
    """ 
    # print(‘Preprocessing text’)

    stop_words = set(stopwords.words('english'))
    stemmed_words = []
    for sent in sentences:
        words = word_tokenize(sent)
        words = [ps.stem(word.lower()) for word in words if word.isalnum()]
        stemmed_words += [word for word in words if word not in stop_words]
    return stemmed_words


