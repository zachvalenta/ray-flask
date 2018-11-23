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
qiu -po 5000 -pa books/<isbn>
```

❌ single - invalid URL
```
qiu -po 5000 -pa books/0000
```

### POST

✅ success
```
qiu -po 5000 -pa books -m POST -j post.json
```

✅ success - key wrong
```
qiu -po 5000 -pa books -m POST -j post-invalid-key-wrong.json
```

❌ fail - key missing
```
qiu -po 5000 -pa books -m POST -j post-invalid-key-missing.json
```

### PUT

✅ success
```
qiu -po 5000 -pa books/0812972864 -m PUT -j put.json
```

❌ fail - JSON (wrong key)
```

```

❌ invalid - JSON (missing key)
```

```
