import match
import re

class post(object):


    def __init__(self, author, hyperlink, text):

        self.post_author = author
        self.post_hyperlink = hyperlink
        self.post_text = re.sub('[\[\]}{*!,:;?()/\&$\n*\+\=_\%]', ' ', text.lower())
        
        self.removequotes(self.post_text)
        self.insertspaces(self.post_text)
        
        self.weight_matches = []
        self.height_matches = []


        
    def removequotes(self, string):
    
        height_regex = re.compile("\d\'\d\"")
        for word in string:
            if height_regex.findall(word) == 0:
                if word[0] == '\"':
                    print string
                    word[0] = ' '
                if word[len(word)-1] == '\"':
                    print string
                    word[len(word)-1] = ' '
                    
    

    # Insert space between 3 digits and adjacent letters
    def insertspaces(self, string):
        components = re.findall( r'(.*\d{1,3})([a-zA-Z.]{2,4}.*)', string)

        if components:
            return self.insertspaces(str(components[0][0] + ' ' + components[0][1]))
        else:
            return string


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
        



