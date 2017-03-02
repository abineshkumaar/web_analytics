# -*- coding: utf-8 -*-
"""
Created on Mon Feb 27 16:01:05 2017

@author: abine
"""
import nltk
from nltk.util import ngrams
import re
from nltk.tokenize import sent_tokenize
from nltk import load

#getTop3 function
list1=[] #empty list definiton
def getTop3(D):
    for key in sorted(D, key=D.get, reverse=True)[:3]:
        list1.append(key) #appending the key to list
    return list1 #returning list
d={"table":20,"chair":12,"pen":10,"pencil":23,"notebook":21,"Book":41} #dictionary definition
print(getTop3(d))  #function call

def loadLexicon(fname):
    newLex=set()
    lex_conn=open(fname)
    #add every word in the file to the set
    for line in lex_conn:
        newLex.add(line.strip())# remember to strip to remove the lin-change character
    lex_conn.close()

    return newLex
    
def processSentence(sentence,posLex,negLex,tagger):
    result=[]
    terms = nltk.word_tokenize(sentence.lower())
    POStags=['NN'] # POS tags of interest 		
    POSterms=getPOSterms(terms,POStags,tagger)
    noun=POSterms['NN']
    posneg = posLex|negLex    
    fourgrams = ngrams(terms, 4)
    for tg in fourgrams:  
        if tg[0]=='not' and tg[2] in posneg and tg[3] in noun: # if the 2gram is a an adverb followed by an adjective
             result.append(tg)
    return result


# return all the terms that belong to a specific POS type
def getPOSterms(terms,POStags,tagger):
	
    tagged_terms=tagger.tag(terms)#do POS tagging on the tokenized sentence

    POSterms={}
    for tag in POStags:POSterms[tag]=set()

    #for each tagged term
    for pair in tagged_terms:
        for tag in POStags: # for each POS tag 
            if pair[1].startswith(tag): POSterms[tag].add(pair[0])

    return POSterms


def run(fpath):

    #make a new tagger
    _POS_TAGGER = 'taggers/maxent_treebank_pos_tagger/english.pickle'
    tagger = load(_POS_TAGGER)

    #read the input
    f=open(fpath)
    text=f.read().strip()
    f.close()

    #split sentences
    sentences=sent_tokenize(text)
    #print ('NUMBER OF SENTENCES: ',len(sentences))

    result=[]

    posLex=loadLexicon('positive-words.txt')
    negLex=loadLexicon('negative-words.txt')

    # for each sentence
    for sentence in sentences:

        sentence=re.sub('[^a-zA-Z\d]',' ',sentence)#replace chars that are not letters or numbers with a spac
        sentence=re.sub(' +',' ',sentence).strip()#remove duplicate spaces

        #tokenize the sentence
           

        
        #posneg=posLex | negLex        
        #POStags=['NN'] # POS tags of interest 		
        #POSterms=getPOSterms(terms,POStags,tagger)

        #noun=POSterms['NN']
        
        result+=processSentence(sentence,posLex,negLex,tagger)
        #get the results for this sentence 
        #adjAfterAdv+=getAdvAdjTwograms(terms, adjectives, adverbs)
        
    return result


if __name__=='__main__':
	print (run('input.txt'))

    