import unittest

import requests


class TestAPI(unittest.TestCase):

    base_url = 'http://127.0.0.1:5000/books'

    def tearDown(self):
        url_clear = '{}/{}'.format(self.base_url, 'clear')
        requests.delete(url_clear)

    def test_get_sanity_check(self):
        res = requests.get(self.base_url)
        self.assertEqual(200, res.status_code)

    def test_get_by_isbn_success(self):
        book = {"name": "foo", "price": 42.00, "isbn": "0374533229"}
        requests.post(self.base_url, json=book)
        isbn = '0374533229'
        url_isbn_lookup = '{}/{}'.format(self.base_url, isbn)
        res = requests.get(url_isbn_lookup)
        self.assertEqual(200, res.status_code)

    def test_get_by_isbn_fail(self):
        isbn = '0000'
        isbn_lookup_url = '{}/{}'.format(self.base_url, isbn)
        res = requests.get(isbn_lookup_url)
        self.assertEqual(404, res.status_code)

    def test_post(self):
        book = {"name": "foo", "price": 42.00, "isbn": "0123456789"}
        res = requests.post(self.base_url, json=book)
        self.assertEqual(201, res.status_code)

    def test_post_invalid_key_missing(self):
        book = {"name": "foo", "price": 42.00, "isbn": "0374533123"}
        res = requests.post(self.base_url, json=book)
        self.assertEqual(201, res.status_code)
