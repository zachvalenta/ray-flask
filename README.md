# OVERVIEW

This repo is a record of working through the course ['Building a REST API Using Python and Flask'](https://app.pluralsight.com/library/courses/python-flask-rest-api/table-of-contents)

📍 I'm using a wrapper around `httpie` I wrote called [qiu](https://github.com/zachvalenta/util-scripts)

# EXAMPLE REQUESTS

__GET__

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

__POST__

✅ single
```
qiu -po 5000 -pa books -m POST -j json/post.json
```

__PUT__

✅ single
```
qiu -po 5000 -pa books/0812972864 -m PUT -j json/put.json
```

__DELETE__

```
qiu -po 5000 -pa books/clear -m DELETE
```
