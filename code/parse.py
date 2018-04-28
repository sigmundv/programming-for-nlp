# -*- coding: utf-8 -*-

import nltk

def read_sentences(_file):
    """
    Read sentences to parse from a text file and store them in a list.
    The sentences are given one per line in the file.

    Input: file name
    Return: list of sentences
    """

    with open(_file, 'r') as sentences:
        return sentences.read().splitlines()


def parse_sentence(sentence, trace=0):
    """
    Using the chart parser from NLTK, parse a given sentence and return an RRG parse tree.

    Input: Sentence, trace (if 0, return only the parse tree, otherwise return intermediate steps)
    Output: Parse tree showing the various constituents of a sentence.
    """

    hline = 30 * '='
    print("\n{0}\n{1}\n{0}".format(hline, sentence))
    
    tokens = sentence.lower().split()
    
    cp = nltk.load_parser("faroese.fcfg", trace=trace)
    
    for tree in cp.parse(tokens):
        print(tree)
    

if __name__ == "__main__":
    trace = 0  # define the trace level; we set it to 0 to only return the final parse tree
    sentences = read_sentences("sentences.txt")  # read in the sentences from the file sentences.txt
    
    for sentence in sentences:  # loop through the sentences and return the parse tree
        parse_sentence(sentence, trace)
