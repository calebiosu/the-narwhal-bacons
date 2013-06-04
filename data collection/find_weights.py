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
    components = re.findall( r'(.*\d{1,3})([a-zA-Z.]{2,4}.*)', string)

    if components:
        return insertspace(str(components[0][0] + ' ' + components[0][1]))
    else:
        return string

# Input check
if not len(sys.argv) == 3:
    print 'Usage: <exec> <word_spread> <post_limit>'
    sys.exit(1)


distance = str(sys.argv[1])
posts = gather_loseit.gathertolist(int(sys.argv[2]))
post_hits = []

weight_exp = r"(( [\b\w .\"\'()-][\d\w\'\"]*[\b\w .\'\"()-]){" + distance + r"}\d{3}[a-zA-Z. ]{1,3}([\w\b\" .\'()-][\d\w\'\"]*[\b\w\" .\'()-]){" + distance + "})"
height_exp
regex = re.compile(exp)


# Search each post for pattern and add matches to same post 
# object's match list, then add post to positive post list.
i = 0
for p in posts:

	# Search post string
    matches = regex.findall(p.post_text)

    if len(matches) > 0:
        
        # Take first group of each tuple match, create new match object
        # and add to post's list of matches
        for elem in matches:
            new_match = match.match(insertspace(elem[0]))
            #new_match = match.match(elem[0])
            p.weight_matches.append(new_match)


        post_hits.append(p)
    
    else:
        print i, ': '
        print p.post_text
    
    i += 1
# Print posts to csv file 
results = open('post_matches_len' + distance + '.csv', 'w')

for p in post_hits:
    p.printpostto(results)

results.close()

print len(post_hits)

