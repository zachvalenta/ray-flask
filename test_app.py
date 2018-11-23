import unittest

import requests


class TestAPI(unittest.TestCase):

    base_url = 'http://127.0.0.1:5000/books'

    def tearDown(self):
        url_clear = '{}/{}'.format(self.base_url, 'clear')
        requests.delete(url_clear)

    def test_GET_200(self):
        res = requests.get(self.base_url)
        self.assertEqual(200, res.status_code)

    def test_GET_200_isbn_lookup(self):
        book = {"name": "foo", "price": 42.00, "isbn": "0374533229"}
        requests.post(self.base_url, json=book)
        isbn = '0374533229'
        url_isbn_lookup = '{}/{}'.format(self.base_url, isbn)
        res = requests.get(url_isbn_lookup)
        self.assertEqual(200, res.status_code)

    def test_GET_404_isbn_lookup(self):
        isbn = '0000'
        isbn_lookup_url = '{}/{}'.format(self.base_url, isbn)
        res = requests.get(isbn_lookup_url)
        self.assertEqual(404, res.status_code)

    # TODO: understand detail of what requests wants here
    def test_POST_201(self):
        book = {"name": "foo", "price": 42.00, "isbn": "0123456789"}
        res = requests.post(self.base_url, json=book)
        self.assertEqual(201, res.status_code)

    def test_POST_201_key_extraneous(self):
        book = {"name": "foo", "price": 42.00, "isbn": "0374533123", "bar": "baz"}
        res = requests.post(self.base_url, json=book)
        self.assertEqual(201, res.status_code)

    def test_POST_400_key_missing(self):
        book = {"name": "foo", "isbn": "0374533123"}
        res = requests.post(self.base_url, json=book)
        self.assertEqual(400, res.status_code)

    def test_PUT_200(self):
        book = {"name": "foo", "price": 42.00, "isbn": "0123456789"}
        requests.post(self.base_url, json=book)
        book_update = {"name": "foo", "price": 43.00, "isbn": "0123456789"}
        url_isbn_lookup = '{}/{}'.format(self.base_url, book['isbn'])
        res = requests.put(url_isbn_lookup, json=book_update)
        self.assertEqual(200, res.status_code)

    def test_PUT_200_key_extraneous(self):
        book = {"name": "alice", "price": 42.00, "isbn": "0374533123"}
        requests.post(self.base_url, json=book)
        book_update = {"name": "alice", "price": 43.00, "isbn": "0374533123", "foo": "bar"}
        url_isbn_lookup = '{}/{}'.format(self.base_url, book_update['isbn'])
        res = requests.put(url_isbn_lookup, json=book_update)
        self.assertEqual(200, res.status_code)

    def test_PUT_404_isbn_lookup(self):
        book = {"name": "foo", "price": 42.00, "isbn": "0123456789"}
        requests.post(self.base_url, json=book)
        book_update = {"name": "foo", "price": 43.00, "isbn": "000"}
        url_isbn_lookup = '{}/{}'.format(self.base_url, book_update['isbn'])
        res = requests.put(url_isbn_lookup, json=book_update)
        self.assertEqual(404, res.status_code)

    def test_PUT_400_key_missing(self):
        book = {"name": "alice", "price": 42.00, "isbn": "0374533123"}
        requests.post(self.base_url, json=book)
        book_update = {"price": 44.00, "isbn": "0374533123"}
        url_isbn_lookup = '{}/{}'.format(self.base_url, book_update['isbn'])
        res = requests.put(url_isbn_lookup, json=book_update)
        self.assertEqual(400, res.status_code)
