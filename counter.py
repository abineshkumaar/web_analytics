# -*- coding: utf-8 -*-
"""
Created on Tue Jan 24 18:43:00 2017

@author: abineshkumar
"""

from collections import Counter
def run(path):
    wordcount={} #dictionary
    

    with open(path) as file: #open the textfile as file
        wordcount = Counter(file.read().lower().split()) #lowercase all text, split and read in the counter
        m= max(wordcount, key=wordcount.get) #getting the key value of most frequent word in the dictionary
        return m #returning the key value to the function call
        
        
print(run('textfile')) #Function call and print the return value from the executed function       
