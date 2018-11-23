import json

from flask import Flask, jsonify, request, Response
from werkzeug.exceptions import abort

# TODO: prevent dupe POST
# TODO: add validations on PUT
# TODO: add PATCH
# TODO: add DELETE
# TODO: sets
# TODO: add error handlers http://flask.pocoo.org/docs/1.0/patterns/apierrors/
# TODO: mimetype necessary each time? if so, store in const
# TODO: 研究 Location header

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


def check_keys_present(req):
    required_keys = {'isbn', 'name', 'price'}
    request_keys = set(req.keys())
    overlap = required_keys.intersection(request_keys) == required_keys
    return True if overlap else False


def handle_extraneous_keys(book):
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
    if check_keys_present(new_book):
        validated_book = handle_extraneous_keys(new_book)
        books.insert(0, validated_book)
        res = Response(json.dumps(new_book), 201, mimetype='application/json')
        res.headers['Location'] = '{}{}'.format('/books/', str(validated_book['isbn']))
        return res
    else:
        return Response('keys missing', 400)


@app.route('/books/<string:isbn>', methods=['PUT'])
def put_book(isbn):
    # TODO: client sending isbn in URL so payload should only be name and price
    new_book = request.get_json()
    book_to_update = lookup_by_isbn(isbn)
    if book_to_update and check_keys_present(new_book):
        validated_book = handle_extraneous_keys(new_book)
        books[books.index(book_to_update)] = validated_book
        return Response(json.dumps(validated_book), 200, mimetype='application/json')
    else:
        abort(404)


@app.route('/books/clear', methods=['DELETE'])
def delete_books():
    books.clear()
    return Response('', 204)
