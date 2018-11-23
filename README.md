# Building a REST API Using Python and Flask

This repo is a record of working through the course ['Building a REST API Using Python and Flask'](https://app.pluralsight.com/library/courses/python-flask-rest-api/table-of-contents)

📍 I'm using a wrapper around `httpie` I wrote called [qiu](https://github.com/zachvalenta/util-scripts)

## EXAMPLE REQUESTS

### GET

✅ all
```
qiu -po 5000 -pa books
```

✅ count
```
qiu -po 5000 -pa books/count
```

✅ single
```
qiu -po 5000 -pa books/0374533229
```

❌ single - invalid URL
```
qiu -po 5000 -pa books/0000
```

### POST

✅ valid
```
qiu -po 5000 -pa books -m POST -j post.json
```

❌ invalid - JSON (wrong key)
```
qiu -po 5000 -pa books -m POST -j post-invalid-key-wrong.json
```

📝 still 200, just throws away extraneous keys on obj creation


❌ invalid - JSON (missing key)
```
qiu -po 5000 -pa books -m POST -j post-invalid-key-missing.json
```

### PUT

✅ valid
```
qiu -po 5000 -pa books/0374533229 -m PUT -j put.json
```

❌ invalid - URL
```

```

❌ invalid JSON (wrong key)
```

```

❌ invalid - JSON (missing key)
```

```
