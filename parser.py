# -*- coding: utf-8 -*-
"""
Created on Mon Feb 13 16:07:40 2017

@author: abineshkumar Kumaravel
"""

from bs4 import BeautifulSoup
import re
import time
import requests

def getCritic(review):
    critic='NA' # initialize critic and text 
    criticChunk=review.find('a',{'href':re.compile('/critic/')})
    if criticChunk: critic=criticChunk.text#.encode('ascii','ignore')
    return critic

def getRating(review):
    rating = 'NA' #Initailize rating to NA
    if (review.find('div',{'class':'review_icon icon small fresh'})):
        return ('fresh')
    elif (review.find('div',{'class':'review_icon icon small rotten'})):
        return ('rotten')
    else:
        return rating


def getSource(review):
    source = 'NA' #Initailize rating to NA
    sourceChunk = review.find('em',{'class':'subtle'})
    if sourceChunk:
        source = sourceChunk.text
    return source
    
def getDate(review):
    date = 'NA' #Initailize rating to NA
    dateChunk = review.find('div',{'class':'review_date'})
    if dateChunk:
        date = dateChunk.text
    return date

    

def getTextLen(review):
    text='NA'
    textChunk=review.find('div',{'class':'the_review'})
    if textChunk: 
        text=textChunk.text#.encode('ascii','ignore')
        text=text.strip()
        return len(text)
    else:   
        return text

def run(url):

    pageNum=1 # number of pages to collect

 	
    for p in range(1,pageNum+1): # for each page 

        print ('page',p)
        html=None

        if p==1: pageLink=url # url for page 1
        else: pageLink=url+'?page='+str(p)+'&sort=' # make the page url
		
        for i in range(5): # try 5 times
            try:
                #use the browser to access the url
                response=requests.get(pageLink,headers = { 'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36', })
                html=response.content # get the html
                break # we got the file, break the loop
            except Exception as e:# browser.open() threw an exception, the attempt to get the response failed
                print ('failed attempt',i)
                time.sleep(2) # wait 2 secs
				
		
        if not html:continue # couldnt get the page, ignore
        
        soup = BeautifulSoup(html.decode('ascii', 'ignore'),'lxml') # parse the html 

        reviews=soup.findAll('div', {'class':re.compile('review_table_row')}) # get all the review divs

        for review in reviews:

            
            print(getCritic(review),' ',getRating(review),' ',getSource(review),' ',getDate(review),' ',getTextLen(review))
 
 
if __name__=='__main__':
    url='https://www.rottentomatoes.com/m/space_jam/reviews/'
    run(url)
