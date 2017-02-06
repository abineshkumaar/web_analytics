# -*- coding: utf-8 -*-
"""
Created on Mon Feb  6 16:14:59 2017

@author: abine
"""

import re
import requests

def run(url, word1): 
    findword = word1.lower() #lowercase the word
    
    freq={} # keep the freq of each word in the file 
    success=False# become True when we get the file

    for i in range(5): # try 5 times
        try:
            #use the browser to access the url 
            response=requests.get(url,headers = { 'User-Agent':'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36', })    
            success=True # success
            break # we got the file, break the loop
        except:
            print ('failed attempt',i)
     
    # all five attempts failed, return  None
    if not success: return None
    
    text=response.text# read in the text from the file
 
    sentences=text.split('.') # split the text into sentences 
	
    for sentence in sentences: # for each sentence 

        sentence=sentence.lower().strip() # loewr case and strip	
        sentence=re.sub('[^a-z]',' ',sentence) # replace all non-letter characters  with a space
		
        words=sentence.split(' ') # split to get the words in the sentence 

        for word in words: # for each word in the sentence 
          if word == findword: #check if the findword is equalto word
              freq[word]=freq.get(word,0)+1
            
    # sort the dictionary by value, in descending order 
    
    for k , v in freq.items():
         return v #return key value
if __name__=='__main__':
    print(run('http://tedlappas.com/wp-content/uploads/2016/09/textfile.txt', "smart"))