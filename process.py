from nltk.tokenize import sent_tokenize
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer

ps = PorterStemmer()

def text_to_words(sentences):
    """
    Process the sentences in text to a list of stemmed words
    """ 
    stop_words = set(stopwords.words('english'))
    stemmed_words = []

    for sent in sentences:
        words = word_tokenize(sent)
        words = [ps.stem(word.lower()) for word in words if word.isalnum()]
        stemmed_words += [word for word in words if word not in stop_words]
    return stemmed_words

def word_frequency_dict(words):
    """
    Creating a dictionary for the frequency of each word.
    """
    freq_dict = dict()
    for word in words:
        if word in freq_dict:
            freq_dict[word] += 1
        else:
            freq_dict[word] = 1
    return freq_dict

def sentence_score_dict(sentences, freq_dict):
    """
    Creating a dictionary to keep the score of each sentence.
    For now, only using the first 15 words of sentence, this part should be modified for more flexibility.
    """
    sent_value = dict()
    for sentence in sentences:
        for word, freq in freq_dict.items():
            if ps.stem(word) in sentence.lower():
                if sentence[:15] in sent_value:
                    sent_value[sentence[:15]] += freq
                else:
                    sent_value[sentence[:15]] = freq
    return sent_value

def average_score(sent_value):
    """
    Calculate average value of a sentence from the original text.
    """
    # sum_values = 0
    # for sentence in sent_value:
    #     sum_values += sent_value[sentence]
    #
    # average = int(sum_values / len(sent_value))
    #
    # return average
    return sum(sent_value.values())/len(sent_value)

def generate_summary(sentences, sent_value, avg):
    """
    Generate a summary sentence for sentence score greater than average.
    15 words for now, need to be modified.
    """
    sentence_count = 0
    summary = ""

    for sent in sentences:
        if sent[:15] in sent_value and sent_value[sent[:15]] >= avg:
            summary += sent + " "
            sentence_count += 1
    return summary