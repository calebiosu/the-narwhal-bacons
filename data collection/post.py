import match
import re

class post(object):


    def __init__(self, author, hyperlink, text):

        self.post_author = author
        self.post_hyperlink = hyperlink
        self.post_text = re.sub('[\[\]}{*!,:;?()/\&$\n*\+\=_\%]', ' ', text.lower())
        
        self.weight_matches = []
        self.height_matches = []


    def printpostto(self, output_file):

        post_header = self.post_id + ',' + self.post_author + ','
        
        for m in self.weight_matches:
            output_file.write(post_header)
            output_file.write(m.match_text + ',' + '\n')
    
    def printforCRF(self, output_file):
        
        for word in self.post_text.split(' '):
            if word != ' ' and word != '\n' and len(word) > 0:
                output_file.write(str(self.post_id) + ','
                        + self.post_hyperlink + ','
                        + word + ',\n')
        



