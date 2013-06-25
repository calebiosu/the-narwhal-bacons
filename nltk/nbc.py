import nltk
import csv
import random

def feature_extractor(post, i):
    
    features = {"SELF": post[i][2]}
   
    
    for n in range(1,6):
        if i-n > len(post):
            features["POS-", n] = post[i-n][2]
        else:
            features["POS-", n] = "N/A"
    
        if i+n < len(post):
            features["POS+", n] = post[i+n][2]
        else:
            features["POS+", n] = "N/A"
            
            
    if i == 0:
        features["POS-1"] = "<START>"
                    
    if i == len(post):
        features["POS+1"] = "<END>"
           
    return features
    


# Corpus formatted as list of posts, each post comprising a list of words, 
# where each word is a list with format: <id_num>, <hyperlink>,  <word>, <tag>.
post_set = []
with open("tagged_matches.csv", "rb") as csvfile:
    
    csv = csv.reader(csvfile)
    reader = [row for row in csv]
    index = 0
    
    while index < len(reader):
        
        post = []
        temp = reader[index][0]
        
        while index < len(reader) and reader[index][0] == temp:
            post.append( (reader[index][:]) )
            index += 1
            
        post_set.append(post)
          
          
          
# Extract features for each word in corpus.
# feature set is a list of tuples: (feature_set, tag)
# where each feature_set is a dictionary
feature_sets = []
for post in post_set:
    for i, line in enumerate(post):
        feature_sets.append( (feature_extractor(post, i), line[3]) ) 
        
random.shuffle(feature_sets)

# training
size = int(len(feature_sets) * 0.1)
train_set, test_set = feature_sets[size:], feature_sets[:size]
classifier = nltk.NaiveBayesClassifier.train(train_set)

# testing
print nltk.classify.accuracy(classifier, test_set)
print classifier.show_most_informative_features(5)


errors = []
positives = []
for (word, tag) in test_set:
    
    guess = classifier.classify(word)
    if guess != tag:
        
        line = "WORD: %-15s TAG: %-10s GUESS: %s" % (word["SELF"], tag, guess)
        errors.append(line)
    
    if guess == tag and guess != '0':
        line = "WORD: %-15s TAG: %-10s" % (word["SELF"], tag)
        positives.append(line)

print "\nERRORS:"
for line in errors:
    print line
    
print "\nPOSITIVES:"
for line in positives:
    print line
       

    