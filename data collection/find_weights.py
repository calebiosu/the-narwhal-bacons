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
if not len(sys.argv) == 2:
    print 'Usage: <exec> <post_limit>'
    sys.exit(1)


posts = gather_loseit.gathertolist(int(sys.argv[1]))
post_hits = []


weight_exp = r"\d{3}"
height_exp = r"\d\'\d\"|\d{2,3} [in|cm|in.|cm.|inches]"
weight_regex = re.compile(weight_exp)
height_regex = re.compile(height_exp)

# Search each post for weight pattern and height pattern.
# Add to list if found.
index = 0
for p in posts:

	# Search post string
    insertspace(p.post_text)
    weight_matches = weight_regex.findall(p.post_text)
    height_matches = height_regex.findall(p.post_text)


    if len(weight_matches) > 0 and len(height_matches) > 0:
        p.post_id = index
        post_hits.append(p)
        index += 1
    



# Print posts to csv file 
results = open('post_matches.csv', 'w')

for p in post_hits:
    p.printforCRF(results)

results.close()


