import match

class post:

    post_author = ''
    post_id = ''
    post_text = ''
    weight_matches = []
    height_matches = []

    postdelimiter = '++++++'

    def __init__(self, author, i_d, text):

        self.post_author = author
        self.post_id = i_d
        self.post_text = text


    def printpostto(self, output_file):

        post_header = self.post_id + '\n' + self.post_author + '\n'
        output_file.write(post_header)
        for m in self.weight_matches:
            output_file.write(m.match_text + '\n')
        output_file.write('\n')



'''    def printpost(self):
        return self.postdelimiter + '\n' + self.post_author + '\n' + self.post_id + '\n' + str(self.weight_matches) + '\n' + self.postdelimiter + '\n'
'''
