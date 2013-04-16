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
# r"\w{0,10}.{0,3}\d{2,3}.{0,3}\w{0,10}"
# r"(([\b\w ,.]\w+[\b\w ,.]){0,5}\d{3}[a-zA-Z.]{0,3}([\b\w ,.]\w+[\w\b ,.]){0,5})"
# uses groups, returns tuples

key1 = r"\w{0,10}.{0,3}\d{2,3}.{0,3}\w{0,10}"
key2 = r"(([\b\w ,.]\w+[\b\w ,.]){0,5}\d{3}[a-zA-Z.]{0,3}([\b\w ,.]\w+[\w\b ,.]){0,5})"
#key3 = 

# function to print matches
# 
def print_matches(posts, key):
    i = 0
    regex = re.compile(key)
    for post in posts:
        i = i+1
        matches = regex.findall(post.post_text)
        print i, ": ",matches
        if (len(matches) > 0):
            post.weight_matches = list(matches)
            results.write(str(post.printpost)+'\n')

print_matches(posts, key1)
print '\n',"<==========================================================>",'\n'
print_matches(posts, key2)

# close file
results.close()
