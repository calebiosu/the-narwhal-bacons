

class post:

	post_author = ''
	post_id = ''
	post_text = ''
	weight_matches = []
	height_matches = []

	postdelimiter = '++++++'

	def __init__(self, post_author, post_id, post_text):
		post_author = post_author
		post_id = post_id
		post_text = post_text

	def printpost():
		return postdelimiter + '\n' + post_author + '\n' + post_id + '\n' + weight_matches + '\n' + postdelimiter + '\n'


