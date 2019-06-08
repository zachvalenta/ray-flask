# TODO

## doing 

- [ ] module 7 - SQLAlchemy

## next

- [ ] module 8 - JWT
- [ ] ER model - http://fastml.com/goodbooks-10k-a-new-dataset-for-book-recommendations/ https://news.ycombinator.com/item?id=19847882
- [ ] testing https://realpython.com/python-testing/#testing-for-web-frameworks-like-django-and-flask + https://julien.danjou.info/db-integration-testing-strategies-python/ + https://github.com/tk0miya/testing.postgresql
- [ ] review modules 1-6

## done

- [x] basic app

# ZA

## example requests

📍 1) bring `httpie` into venv so you can run w/ `venv` activated 2) bring these req into `Makefile`

__GET__

```
qiu -po 5000 -pa books
```

```
qiu -po 5000 -pa books/count
```

```
qiu -po 5000 -pa books/<isbn>
```

__POST__

```
qiu -po 5000 -pa books -m POST -j json/post.json
```

__PUT__

```
qiu -po 5000 -pa books/0812972864 -m PUT -j json/put.json
```

__PATCH__

```
qiu -po 5000 -pa books/0812972864 -m PATCH -j json/patch.json
```

__DELETE__

```
qiu -po 5000 -pa books/0812972864 -m DELETE
```
