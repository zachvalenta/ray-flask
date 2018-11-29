import json

from flask import Flask, jsonify, request, Response

# TODO: swap out `jsonify()`
# TODO: add PATCH
# TODO: add DELETE
# TODO: POST/PUT n -> rf PUT to use isbn from URL
# TODO: 研究 Location header, sets, mimetype

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
        return Response('no book found', 404)


@app.route('/books', methods=['POST'])
def post_book():
    new_book = request.get_json()
    book_exists = lookup_by_isbn(new_book['isbn'])
    if book_exists:
        return Response('book already exists', 400)
    if not check_keys_present(new_book):
        return Response('keys missing', 400)
    validated_book = handle_extraneous_keys(new_book)
    books.insert(0, validated_book)
    res = Response(json.dumps(new_book), 201, mimetype='application/json')
    res.headers['Location'] = '{}{}'.format('/books/', str(validated_book['isbn']))
    return res


@app.route('/books/<string:isbn>', methods=['PUT'])
def put_book(isbn):
    new_book = request.get_json()
    book_to_update = lookup_by_isbn(isbn)
    if not book_to_update:
        return Response('no book to update', 404)
    if not check_keys_present(new_book):
        return Response('keys missing', 400)
    else:
        validated_book = handle_extraneous_keys(new_book)
        books[books.index(book_to_update)] = validated_book
        return Response(json.dumps(validated_book), 200, mimetype='application/json')


@app.route('/books/<string:isbn>', methods=['PATCH'])
def patch_price(isbn):
    new_price = request.get_json()['price']
    book_to_update = lookup_by_isbn(isbn)
    if not book_to_update:
        return Response('no book to update', 404)
    else:
        book_to_update['price'] = new_price
        return Response(json.dumps(book_to_update), 200, mimetype='application/json')


@app.route('/books/clear', methods=['DELETE'])
def delete_books():
    books.clear()
    return Response('', 204)
