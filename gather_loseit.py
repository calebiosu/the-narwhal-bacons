'''
Created on Apr 8, 2013
@author: Alex Shilen
'''


''' Script for gathering N posts from r/loseit '''

import praw
import sys
import post


r = praw.Reddit(user_agent='obesity_detection_app')
loseit_subreddit = r.get_subreddit('loseit')


def gathertolist(lim):
    post_list = []
    for submission in loseit_subreddit.get_new(limit = lim):
        newpost = post.post(str(submission.author),
            submission.short_link,
            submission.selftext.lower())
        post_list.append(newpost)


    return post_list

def gathertofile(lim, filename):

    f = open(filename, 'w')
    post_delimiter = '++++++'

    for submission in loseit_subreddit.get_new(limit = lim):
        f.write('\n' + post_delimiter +                            
            '\n' + submission.title.encode('utf-8') + 
            '\n' + str(submission.author).encode('utf-8') +
            '\n' + submission.short_link.encode('utf-8') + 
            '\n' + submission.selftext.encode('utf-8'))


    f.write('\n' + post_delimiter)
    f.close()  
    
if __name__ == "__main__":    
    
    if not len(sys.argv) == 3:
        print 'Usage: <exec> <post_limit> <file_name>'

    gathertofile(int(sys.argv[1]), sys.argv[2])







