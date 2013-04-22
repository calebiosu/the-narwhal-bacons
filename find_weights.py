import sys
import re
import post
import gather_loseit
import match


''' Script finds weights in a list of posts with up to N words 
    on either side, turns them into match objects, adds the 
    match objects to a list within each post object and prints 
    each post to a file. '''

# Insert space between 3 digits and adjacent letters
def insertspace(string):
    components = re.findall( r'(.*\d{3})([a-zA-Z.]{3,4}.*)', string)

    if components:
        return str(components[0][0] + ' ' + components[0][1])
    else:
        return string

# Input check
if not len(sys.argv) == 2:
    print 'Usage: <exec> <int>'
    sys.exit(1)


distance = str(sys.argv[1])
posts = gather_loseit.gathertolist(100)
post_hits = []

exp = r"(?=(([\b\w .\"'()-]\w*[\b\w .'\"()-]){" + distance + r"}\d{3}[a-zA-Z.]{0,3}([\w\b\" .'()-]\w*[\b\w\" .'()-]){" + distance + "}))"
regex = re.compile(exp)


# Search each post for pattern and add matches to same post 
# object's match list, then add post to positive post list.
for p in posts:

	# Search post string
    matches = regex.findall(p.post_text)

    if matches:

	    
        # Take first group of each tuple match, create new match object
        # and add to post's list of matches
        for elem in matches:
            new_match = match.match(insertspace(elem[0]))
            p.weight_matches.append(new_match)


        post_hits.append(p)


# Print posts to file 
results = open('post_matches_len' + distance, 'w')

for p in post_hits:
    p.printpostto(results)

results.close()


