# TODO

🔗 https://github.com/zachvalenta/flask-rest-api/

## doing 

- [ ] gunicorn / Nginx

## next

- [ ] db - sqlite3
- [ ] db - `m test` - start app, run tests, tear down in-mem db
- [ ] JWT
- [ ] db - Flask tutorial for more realistic setup
- [ ] db - `m test` - replace first impl
- [ ] ER model - replace `bookshelf-*.md` (`is_current`) -> http://fastml.com/goodbooks-10k-a-new-dataset-for-book-recommendations/)
- [ ] db - SQLAlchemy

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
