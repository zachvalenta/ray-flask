from flask import Flask, jsonify, request, Response
from werkzeug.exceptions import abort

# TODO: .json to own folder
# TODO: differentiate dummy data across .json
# TODO: integration tests using .json

"""
NOTES

* definition of a framework: receive req, route to controller, dispatch from controller, return res
* jsonify also handles headers
* docs 1.3.2 say use `SimpleJSON`, why is course using `jsonify`?
* when did they get rid of the `app.run(port=5000)` bit?
* JWT -> https://github.com/vimalloc/flask-jwt-extended

"""

app = Flask(__name__)

# IN-MEM DATA STORE


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

# UTIL


def handle_invalid_post_key_missing(book):
    if 'name' in book and 'price' in book and 'isbn' in book:  # idky but Flask complains if not on one-line
        return True
    else:
        return False


def handle_invalid_post_key_wrong(book):
    """point here is to exclude any extraneous keys"""
    return {
        'name': book['name'],
        'price': book['price'],
        'isbn': book['isbn'],
    }

# ROUTES


@app.route('/books')
def get_books():
    return jsonify({'books': books})


@app.route('/books/<string:isbn>')
def get_book(isbn):
    for book in books:
        if book['isbn'] == isbn:
            return jsonify({'book': book})
        return abort(404)


@app.route('/books', methods=['POST'])
def add_book():
    new_book = request.get_json()
    if handle_invalid_post_key_missing(new_book):
        validated_book = handle_invalid_post_key_wrong(new_book)
        books.insert(0, validated_book)
        res = Response('', 201, mimetype='application/json')
        # TODO: why does this mangle the ISBN
        # res.headers['Location'] = '{} {}'.format('/books/', validated_book['isbn'])
        res.headers['Location'] = '/books/' + str(validated_book['isbn'])
        return res

    else:
        # TODO: mv to else of handle_invalid_post_key_missing
        return abort(400)
