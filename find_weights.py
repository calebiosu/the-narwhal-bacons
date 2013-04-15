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

regex = re.compile(r"\w{0,10}.{0,3}\d{2,3}.{0,3}\w{0,10}")

for post in posts:
    m = regex.match(post.post_text)
    print matches
    if (len(matches) > 0):
        post.weight_matches = list(matches)
        results.write(str(post.printpost))
