# -*- coding: utf-8 -*-
"""
Created on Mon Jan 30 15:59:17 2017

@author: abine
"""
from collections import Counter
def loadLexicon(fname):
    newLex=set()
    lex_conn=open(fname)
    #add every word in the file to the set
    for line in lex_conn:
        newLex.add(line.strip())# remember to strip to remove the lin-change character
    lex_conn.close()

    return newLex

def run(path):
    #load the positive lexicons
    dictionary={}
    posLex=loadLexicon('positive-words.txt')
    fin=open(path)
    for line in fin: # for every line in the file (1 review per line)
        positive=set() 
        line=line.lower().strip()   
        words=line.split(' ') # slit on the space to get list of words
          
        for word in words: #for every word in the review
            if word in posLex: # if the word is in the positive lexicon
                positive.add(word) #add the word in positive set
               
                
        for word in positive:   #check if the word is in positive set
            if word in dictionary: #check if the word is in dictionary already
                dictionary[word] = dictionary[word]+1 #add the word to the dictionary
            else:
                dictionary[word]=1

    fin.close()
    return dictionary 


if __name__ == "__main__": 
    dictionary1={}
    dictionary=run('textfile')
    print (dictionary)
