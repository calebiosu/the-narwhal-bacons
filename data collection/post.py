import match
import re

class post(object):


    def __init__(self, author, hyperlink, text):

        self.post_author = author
        self.post_hyperlink = hyperlink
        self.post_text = re.sub('[\[\]}{*!:;?()/\&$\n*\+\=_\%,]', ' ', text.lower())
        
        self.seperatedashes()
        self.removequotes()
        self.insertspaces()
        self.tokenizeperiods()
        
        self.weight_matches = []
        self.height_matches = []


        
    def removequotes(self):
    
        newpost = ''
        for word in self.post_text.split(' '):
            
            if not re.search("\d\"", word):
                word = word.replace('\"', '')             
                  
            newpost += word + ' '
        self.post_text = newpost
    

    # Insert space between 3 digits and adjacent letters
    def insertspaces(self):
        
        components = re.findall( r'(.*\d{1,3})([a-zA-Z.]{2,4}.*)', self.post_text)
        if components:
            self.post_text = str((components[0][0] + ' ' + components[0][1]))
            return self.insertspaces()
        else:
            return self.post_text

    def tokenizeperiods(self):
        
        newpost = ''
        for word in self.post_text.split(' '):
            
            if re.search('[\"a-zA-z]\.', word):
                word = word.replace('.', ' .')
                
            if re.search('\.[a-zA-z]', word):
                word = word.replace('.', '. ')
                
            newpost += word + ' '
        
        self.post_text = newpost
        

    def seperatedashes(self):
        
        newpost = ''
        for word in self.post_text.split(' '):
            
            if re.search('-', word):
                word = word.replace('-', ' - ')
                
            newpost += word + ' '
        self.post_text = newpost
        
        
        
    def printpostto(self, output_file):

        post_header = self.post_id + ',' + self.post_author + ','
        
        for m in self.weight_matches:
            output_file.write(post_header)
            output_file.write(m.match_text + ',' + '\n')
    
    
    @staticmethod
    def tag(string):
        
        if not re.search('\d{3}', string) and not re.search(r"\d\'\d\"|\d{2,3}.in|cm|in\.|cm\.|inches", string):
            return str(0)
        return ''
        
    
    def printforCRF(self, output_file):
        
        for word in self.post_text.split(' '):
            if word != ' ' and word != '\n' and len(word) > 0:
                output_file.write(str(self.post_id) + ','
                        + self.post_hyperlink + ','
                        + word + ',' 
                        + post.tag(word) + ',\n')
        



