import re

class match:

    match_text = ''
    isConfirmed = False
    '''
    # Insert space between 3 digits and adjacent letters
    def insertSpaces(self, string):
        components = re.findall(r'(.*\d{3})([a-zA-Z.]{3,4}.*)', string)

        if components:
            match_text = str(components[0][0] + ' ' + components[0][1])   
    ''' 
    def __init__(self, text):
        self.match_text = text
        #self.insertSpaces(text)
