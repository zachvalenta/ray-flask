from flask import Flask, jsonify, request

"""
NOTES

* definition of a framework: receive req, route to controller, dispatch from controller, return res
* jsonify also handles headers
* docs 1.3.2 say use `SimpleJSON`, why is course using `jsonify`?
* when did they get rid of the `app.run(port=5000)` bit?
* JWT -> https://github.com/vimalloc/flask-jwt-extended

"""

app = Flask(__name__)

books = [
	{
		'name': 'Origins of Political Order',
		'price': 10.00,
		'isbn': '0374533229',
	},
	{
		'name': 'Political Order and Political Decay',
		'price': 10.00,
		'isbn': '0374535620',
	}
]


@app.route('/')
def hello_world():
	return 'hey zv'


@app.route('/books')
def get_books():
	return jsonify({'books': books})


@app.route('/books/<string:isbn>')
def get_book(isbn):
	for book in books:
		if book['isbn'] == isbn:
			return jsonify({'book': book})
	return 'could not find book'


def validate_book(book):
	if 'name' in book and 'price' in book and 'isbn' in book:  # idky but Flask complains if not on one-line
		return True
	else:
		return False


@app.route('/books', methods=['POST'])
def add_book():
	return jsonify(request.get_json())

# TODO: add tests

