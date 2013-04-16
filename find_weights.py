import sys
import re
import post
import gather_loseit

# \d{2,3}.*?\b[\w+?\b]{2}

results = open('loseit_posts_weights', 'w')
posts = gather_loseit.gathertolist(100)

# still working on regex
# at the moment it grabs 2-3 numbers with 
# 3 characters of any kind on either side plus
# 10 more word (\w) characters in both directions.

# the problem right now is in using * or + with \w
# in order to search for an arbitrary number of \w
# characters (a word of arbitrary size) N times

# python doesn't seem to like \w* or \w+

regex = re.compile(r"(([\b\w .]\w*[\b\w .]){0,4}\d{3}[a-zA-Z.]{0,3}([\b\w .]\w*[\b\w .]){0,4})")


for post in posts:
    match = regex.findall(post.post_text)
    if match:
        print match, '\n' + 'TEXT::::::::::::::::'
        print post.post_text
        '''
        if (len(matches) > 0):
        post.weight_matches = list(matches)
        results.write(str(post.printpost))
'''

