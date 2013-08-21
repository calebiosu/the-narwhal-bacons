import nltk
import csv
import random
import conf_matrix
import re


def is_number(s):
    try:
        float(s)
        return True
    except ValueError and TypeError:
        return False
         

def feature_extractor(post, i, history):
    
    features = {"SELF": post[i][2]}
    
    
    if is_number(post[i]):
        features["is_number"] = True
    else:
        features["is_number"] = False
    
    for n in range(1,6):
        if i-n > 0:
            features["POS-%d" %n] = post[i-n][2]
            features["POS-%d TAG" %n] = history[i-n]
        else:
            features["POS-%d" %n] = "N/A"
            features["POS-%d TAG" %n] = "N/A"
    
        if i+n < len(post):
            features["POS+%d" %n] = post[i+n][2]
        else:
            features["POS+%d" %n] = "N/A"
            
            
    if i == 0:
        features["POS-1"] = "<START>"
                    
    if i == len(post):
        features["POS+1"] = "<END>"
           
    return features
    
def compile_post_set():

    # Corpus formatted as list of posts, each post comprising a list of words, 
    # where each word is a list with format: <id_num>, <hyperlink>,  <word>, <tag>.
    post_set = []
    with open("tagged_matches.csv", "rb") as csvfile:
    
        new_csv = csv.reader(csvfile)
        reader = [row for row in new_csv]
        index = 0
    
        while index < len(reader):
        
            post = []
            temp = reader[index][0]
        
            while index < len(reader) and reader[index][0] == temp:
                post.append( (reader[index][:]) )
                index += 1
            
            post_set.append(post)

    return post_set


class ConsecutivePosTagger(nltk.TaggerI):
    
    
    # Extract features for each word in corpus.
    # training set is a list of tuples: (feature_set, tag)
    # where each feature_set is a dictionary
    def __init__(self, post_set):
        training_sets = []
        words = []
        for post in post_set:
            history = []
            for i, line in enumerate(post):
                feature_set = feature_extractor(post, i, history) 
                training_sets.append( (feature_set, line[3]) )
                history.append(line[3])
        self.classifier = nltk.NaiveBayesClassifier.train(training_sets)
        for (id_num, hyperlink, word, tag) in post:
            words.append(word)

        
    def tag(self, post):
        history = []
        for i, word in enumerate(post):
            feature_set = feature_extractor(post, i, history)
            tag = self.classifier.classify(feature_set)
            history.append(tag)
       
        return zip(words, history)






          
if __name__ == "__main__":
    

    post_set = compile_post_set()
    testing_set = []
    
    for post in post_set:
        test_set = []
        for (id_num, hyperlink, word, tag) in post:
            test_set.append( (word, tag) )
        testing_set.append(test_set)
            
    print testing_set

    size = int(len(post_set) * 0.1)
    training_set = post_set[size:]
    tagger = ConsecutivePosTagger(training_set)
    print tagger.evaluate(testing_set)








