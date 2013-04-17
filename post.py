import match

class post(object):

    postdelimiter = '++++++'

    def __init__(self, author, i_d, text):

        self.post_author = author
        self.post_id = i_d
        self.post_text = text
        self.post_text = self.post_text.replace('\n', ' ')
        
        self.weight_matches = []
        self.height_matches = []


    def printpostto(self, output_file):

        post_header = self.post_id + '\n' + self.post_author + '\n'
        output_file.write(post_header)
        for m in self.weight_matches:
            output_file.write(m.match_text + '\n')
        output_file.write('\n')



'''    def printpost(self):
        return self.postdelimiter + '\n' + self.post_author + '\n' + self.post_id + '\n' + str(self.weight_matches) + '\n' + self.postdelimiter + '\n'
'''
