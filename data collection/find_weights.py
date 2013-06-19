import sys
import re
import post
import gather_loseit
import match


''' Script finds posts that contain both potential weight and potential
height matches found by regex. It then adds them to a csv file. '''



# Input check
if not len(sys.argv) == 2:
    print 'Usage: <exec> <post_limit>'
    sys.exit(1)


posts = gather_loseit.gathertolist(int(sys.argv[1]))
hits = []

weight_exp = r"\d{3}"
height_exp = r"\d\'\d\"|\d{2,3}.in|cm|in\.|cm\.|inches"
weight_regex = re.compile(weight_exp)
height_regex = re.compile(height_exp)

# Search each post for weight pattern and height pattern.
# Add to list if found.

i = 1
for p in posts:

	# Search post string
    weight_matches = weight_regex.findall(p.post_text)
    height_matches = height_regex.findall(p.post_text)


    if len(weight_matches) > 0 and len(height_matches) > 0:
        p.post_id = i
        hits.append(p)
        i += 1

# Print posts to csv file 
results = open('matches.csv', 'w')
for p in hits:
    p.printforCRF(results)

    
results.close()


