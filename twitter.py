# -*- coding: utf-8 -*-
"""
Created on Wed Feb 22 16:27:15 2017

@author: abine
"""

"""
The script visits the profile of a given twitter user, scrolls down the screen twice to load more tweets,
and then write the text and number of likes for each tweet to a file.
"""


from selenium import webdriver
import time


url='https://twitter.com/SHAQ'

#open the browser and visit the url
driver = webdriver.Chrome('chromedriver.exe')
driver.get(url)

#scroll down twice to load more tweets
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
time.sleep(2)
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
time.sleep(2)

#find all elements with a class that ends in 'tweet-text'
tweets=driver.find_elements_by_css_selector("[data-item-type=tweet]")

"""
for tweet in tweets:
    print (tweet.find_element_by_css_selector("[class$=tweet-text"))
"""

#write the tweets to a file
fw=open('tweets.txt','w',encoding='utf-8')
for tweet in tweets:
    txt,retweets,favourites,replies,date='NA','NA','NA','NA','NA'
#text    
    try: 
        txt=tweet.find_element_by_css_selector("[class$=tweet-text]").text
    except: 
        print ('no text')     
#retweets
    try:
        retweetElement=tweet.find_element_by_css_selector("[class$=js-actionRetweet]")
        retweets=retweetElement.find_element_by_css_selector('[class=ProfileTweet-actionCountForPresentation]').text                                      
    except:
        print ('no retweets')

#Favourites    
    try: 
        favouritesElement=tweet.find_element_by_css_selector("[class$=js-actionFavorite]")
        favourites=favouritesElement.find_element_by_css_selector('[class=ProfileTweet-actionCountForPresentation]').text                                    
    except: print ('no Favourites')     
#replies
    try: 
        repliesElement=tweet.find_element_by_css_selector("[class$=js-actionReply]")
        replies=repliesElement.find_element_by_css_selector('[class=ProfileTweet-actionCountForPresentation]').text                                    
    except: print ('no Replies')
#date
    try: 
        dateElement=tweet.find_element_by_css_selector("[class$=time]")
        date=dateElement.find_element_by_css_selector('[data-long-form="true"]').text                                    
    except: print ('no Date')
    
    fw.write(txt.replace('\n',' ')+'\t'+str(retweets)+'\t'+str(favourites)+'\t'+str(replies)+'\t'+str(date)+'\n')



fw.close()


driver.quit()#close the browser
