import nltk
from nltk.tokenize import sent_tokenize
import sys
import process
import frequency


def main():

    if len(sys.argv) == 2:
        # When file is given in a way: python main.py filename
        return
    else:
        # In case, it's given as an address, then perform some scrapping.

        # Get the text/article from the Internet or prompt the user
        text = "Some text from main file"

        # sentence-tokenized copy of text
        sentences = sent_tokenize(text)
        sentences_num = len(sentences)



if __name__ == '__main__':
    main()