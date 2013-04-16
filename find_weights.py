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


# progress:
# r"(([\b\w ,.]\w+[\b\w ,.]){0,5}\d{3}[a-zA-Z.]{0,3}([\b\w ,.]\w+[\w\b ,.]){0,5})"
# uses groups, returns tuples

regex = re.compile(r"(([\b\w .]\w*[\b\w .]){0,4}\d{3}[a-zA-Z.]{0,3}([\b\w .]\w*[\b\w .]){0,4})")

for post in posts:
    matches = regex.findall(post.post_text)
    print matches
    if (len(matches) > 0):
        post.weight_matches = list(matches)
        results.write(str(post.printpost))

# close file
results.close()
