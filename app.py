from flask import Flask, jsonify, request

# jsonify also handles headers

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


@app.route('/books', methods=['POST'])
def add_book():
	return jsonify(request.get_json())
