"""
Construct a feature matrix of the labeled file.

"""

import os
import sys
import csv
from collections import defaultdict


words = defaultdict(int)
labels = list()

reader = csv.reader(open(sys.argv[1]))
# this is matching the commma-delimited entries in csv and assigninng 
for url, username, post, label in reader:
    
    for word in post.split(' '): # split post with spaces to make words
        if word != '':
            words[word] += 1 # keeps track of the number the times words with dictionary
    
    labels.append(int(label)) # 1 or 0 indicating 

print >> sys.stderr, "Found %d distinct words with %d positively labeled." % (len(words), sum(labels))

print >> sys.stderr, "  %d of which are used more than once." % len([w for w,c in words.items() if c > 1]) # 
print >> sys.stderr, "  %d of which are used more than once." % len([w for w,c in words.items() if c > 8])

# a list of tuple list is sorted by the first element in the sublist
counted_words_sorted = sorted([(c,w) for w,c in words.items()])
counted_words_sorted.reverse()

outfh = open('feature_matrix.csv', 'w')
writer = csv.writer(outfh)

reader = csv.reader(open(sys.argv[1]))
for url, username, post, label in reader:
    writer.writerow([label] + [1 if word in post.split(' ') else 0 for cnt, word in counted_words_sorted])

outfh.close()

for i, (count, word) in enumerate(counted_words_sorted):
    print >> sys.stderr, "%d:   `%s`      %d" % (i+1, word, count)
    if i > 20:
        break

# lamdbda functions - inline definitions of a 
    