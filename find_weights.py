import sys
import re
import post
import gather_loseit

# \d{2,3}.*?\b[\w+?\b]{2}
#[\w\.]{2}.*?\d{2,3}.*?[\w\.]{2}
results = open('loseit_posts_weights', 'w')
posts = gather_loseit.gathertolist(100)


for post in posts:
    matches = re.findall("\d{2,3}", post.post_text, 0)
    if (len(matches) > 0):
        post.weight_matches = matches
        results.write(post.printpost())



