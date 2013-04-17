import sys
import re
import post
import gather_loseit
import match


''' Script finds weights in a list of posts with up to N words 
    on either side, turns them into match objects, adds the 
    match objects to a list within each post object and prints 
    each post to a file. '''


# input check
if not len(sys.argv) == 2:
    print 'Usage: <exec> <int>'
    sys.exit(1)


distance = str(sys.argv[1])
posts = gather_loseit.gathertolist(100)
post_hits = []

exp = r"(([\b\w .'()-]\w*[\b\w .'()-]){0," + distance + r"}\d{3}[a-zA-Z.]{0,3}([\b\w .'()-]\w*[\b\w .'()-]){0," + distance + "})"
regex = re.compile(exp)


for p in posts:

    matches = regex.findall(p.post_text)
    if matches:
        
        # Take first group of each tuple match, create new match object
        # and add to post's list of matches
        for elem in matches:
            new_match = match.match(elem[0])
            p.weight_matches.append(new_match)

    post_hits.append(p)


# Print posts to file 
results = open('post_matches_len' + distance, 'w')

for p in post_hits:
    p.printpostto(results)

results.close()
