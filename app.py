import json

from flask import Flask, jsonify, request, Response
from werkzeug.exceptions import abort

# TODO: `requests` to test README endpoints
# TODO: endpoint to clear all data
# TODO: integration tests using .json
# TODO: prevent dupe POST
# TODO: add validations on PUT
# TODO: add PATCH
# TODO: add DELETE
# TODO: .json to own folder
# TODO: mimetype necessary each time? if so, store in const

"""
NOTES

* definition of a framework: receive req, route to controller, dispatch from controller, return res
* `jsonify()` dict ➡️ json, add HTTP headers
* `request.json` returns dict
* docs 1.3.2 say use `SimpleJSON`, why is course using `jsonify`?
* when did they get rid of the `app.run(port=5000)` bit?
* JWT -> https://github.com/vimalloc/flask-jwt-extended

"""

app = Flask(__name__)


# UTIL

books = []


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


def lookup_by_isbn(lookup):
    for book in books:
        if book['isbn'] == lookup:
            return book

# ROUTES


@app.route('/books')
def get_books():
    return jsonify({'books': books})


@app.route('/books/count')
def get_books_count():
    return jsonify({'book_count': len(books)})


@app.route('/books/<string:isbn>')
def get_book(isbn):
    book_found = lookup_by_isbn(isbn)
    if book_found:
        return jsonify({'book': book_found})
    else:
        err_msg = {'error': 'invalid isbn'}
        res = Response(json.dumps(err_msg), 404, mimetype='application/json')
        return res


@app.route('/books', methods=['POST'])
def post_book():
    new_book = request.get_json()
    if handle_invalid_post_key_missing(new_book):
        validated_book = handle_invalid_post_key_wrong(new_book)
        books.insert(0, validated_book)
        # TODO: mimetype, research HTTP 'Location' header -> should you also be returning JSON of created?
        res = Response(json.dumps(new_book), 201, mimetype='application/json')
        res.headers['Location'] = '{}{}'.format('/books/', str(validated_book['isbn']))
        return res

    else:
        # TODO: mv to else of handle_invalid_post_key_missing
        return abort(400)


@app.route('/books/<string:isbn>', methods=['PUT'])
def put_book(isbn):
    # TODO client sending isbn in URL so payload should only be name and price
    new_book = request.get_json()
    book_to_update = lookup_by_isbn(isbn)
    # TODO validate, add 204 status code
    if book_to_update:
        books[books.index(book_to_update)] = new_book
        return jsonify({'book': new_book})
    else:
        abort(404)


@app.route('/books/clear', methods=['DELETE'])
def delete_books():
    books.clear()
    return Response('', 204)
