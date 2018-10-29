# Building a REST API Using Python and Flask

This repo is a record of working through the course ['Building a REST API Using Python and Flask'](https://app.pluralsight.com/library/courses/python-flask-rest-api/table-of-contents)

## hit endpoints

📍 I'm using a wrapper around `httpie` I wrote called [qiu](https://github.com/zachvalenta/util-scripts)

__GET__

```
qiu -po 5000 -pa books/0374533229
```

__POST__

```
qiu -po 5000 -m POST -j post.json -pa books
```

