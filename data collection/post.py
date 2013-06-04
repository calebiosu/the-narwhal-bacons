import match
import re

class post(object):


    def __init__(self, author, hyperlink, i_d, text):

        self.post_author = author
        self.post_hyperlink = hyperlink
        self.post_id = i_d
        self.post_text = re.sub('[\[\]}{*!,:;?()/\&$\n*\+\=_\%]', ' ', text.lower().encode('utf8'))
        
        self.weight_matches = []
        self.height_matches = []


    def printpostto(self, output_file):

        post_header = self.post_id + ',' + self.post_author + ','
        
        for m in self.weight_matches:
            output_file.write(post_header)
            output_file.write(m.match_text + ',' + '\n')
    
    def printforCRF(self, output_file):
        
        for word in self.post_text.split(' '):
            output_file.write(self.post_id , ','
                    + self.post_hyperlink + ','
                    + word + ',\n')
        



