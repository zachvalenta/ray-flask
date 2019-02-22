# TODO

🔗 https://github.com/zachvalenta/flask-rest-api/

🔗 `/Users/zach/Desktop/zvmac/materials/sw/za/data/bookcase`

📍 replace `bookshelf-*.md` (`is_current`) and `~/bin/shugui`

## doing 

- [ ] gunicorn / Nginx

> 📍 think this needs further work because still passing requests through to Flask dev server -> https://stackoverflow.com/q/13596558/6813490

## next

- [ ] db - SQLAlchemy
- [ ] JWT
- [ ] db - ER model - http://fastml.com/goodbooks-10k-a-new-dataset-for-book-recommendations/)

---

- [ ] db - sqlite3 🔗 `db.md`
- [ ] db - Flask tutorial for more realistic setup
- [ ] [host on Linode](https://www.youtube.com/watch?v=LUFn-QVcmB8)
- [ ] db - start app, run tests, tear down in-mem db https://realpython.com/python-testing/

* 🔗 `testing.md`
* test db https://julien.danjou.info/db-integration-testing-strategies-python/ + setup temp db and teardown after test https://stackoverflow.com/a/29822459/6813490

## done

- [x] basic app

# ZA

## example requests

__GET__

```
qiu -po 5000 -pa books
```

📍 [qiu](https://github.com/zachvalenta/qiu) is just a wrapper I wrote around [httpie](https://github.com/jakubroztocil/httpie)

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
