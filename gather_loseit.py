'''
Created on Apr 8, 2013

@author: fluffyfirebreathingbunny
'''
'''
Created on Apr 8, 2013

@author: fluffyfirebreathingbunny
'''

# TODO:
# Regex for height / weight
# \d{2,3}.*?\b[\w+?\b]{2}

import praw
import re


r = praw.Reddit(user_agent='obesity_detection_app')
loseit_subreddit = r.get_subreddit('loseit')

i = 0;
f = open("loseit_posts", "w")

for submission in loseit_subreddit.get_new(limit=100):
    # print first 20 submissions on new page
    print i
    f.write ( "\n----------------------------------------\n" + submission.selftext.lower())
    i+=1
    print submission.short_link
    print submission.title 
    weights = re.findall("(\d*\.?\d+)\s?(\w+)", submission.selftext)
    for line in weights:
        print line
   
    
    
    
    