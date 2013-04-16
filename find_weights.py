import sys
import re
import post
import gather_loseit

# input check
if not len(sys.argv) == 2:
    print 'Usage: <exec> <int>'

results = open('loseit_posts_weights', 'w')
posts = gather_loseit.gathertolist(100)

exp = r"(([\b\w .']\w*[\b\w .']){0," + str(sys.argv[1]) + r"}\d{3}[a-zA-Z.]{0,3}([\b\w .']\w*[\b\w .']){0," + str(sys.argv[1]) + "})"

regex = re.compile(exp)


for p in posts:
    match = regex.findall(p.post_text)
    if match:
        print match, '\n' + 'TEXT::::::::::::::::'
        print p.post_id
        print p.post_text

        if (len(match) > 0):
            p.weight_matches = list(match)
            result = p.printpost()
            results.write(result)

# close file
results.close()
