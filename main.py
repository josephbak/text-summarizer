import nltk
from nltk.tokenize import sent_tokenize
import process
import frequency


def main():
    # Get the text/article from the Internet or prompt the user
    text = "Some text from main file"

    # sentence-tokenized copy of text
    sentences = sent_tokenize(text)
    sentences_num = len(sentences)



if __name__ == '__main__':
    main()