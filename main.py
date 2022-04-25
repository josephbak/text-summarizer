import nltk
import sumy
from nltk.tokenize import sent_tokenize
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lex_rank import LexRankSummarizer
from sumy.summarizers.luhn import LuhnSummarizer
from sumy.summarizers.lsa import LsaSummarizer

import sys
import process
import frequency



def main():

    # Load the file
    if len(sys.argv) == 2:
        # When file is given in a way: python main.py filename
        with open (sys.argv[1]) as f:
            text = f.read()
    else:
        # In case, it's given as an address, then perform some scrapping.

        # Get the text/article from the Internet or prompt the user
        text = "Some text from main file"

        # sentence-tokenized copy of text
        sentences = sent_tokenize(text)
        sentences_num = len(sentences)

    # Parsing
    parser = PlaintextParser.from_string(text,Tokenizer("english"))

    # Using Frequency
    # freq_sentence = 


    # Using LexRank algorithm
    lex_summarizer = LexRankSummarizer()
    #Summarize the document with 2 sentences
    lex_summary = lex_summarizer(parser.document, 2)
    print("Lexrank summary:")
    for sentence in lex_summary:
        print(sentence)

    # Using Luhn algorithm
    luhn_summarizer = LuhnSummarizer()
    luhn_summary = luhn_summarizer(parser.document,2)
    print("Luhn summary:")
    for sentence in luhn_summary:
        print(sentence)
    
    # Latent Semantic Analysis (LSA)


if __name__ == '__main__':
    main()