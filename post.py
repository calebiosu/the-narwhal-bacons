

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

    def printpost():
        return postdelimiter + '\n' + post_author + '\n' + post_id + '\n' + weight_matches + '\n' + postdelimiter + '\n'

