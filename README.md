# example requests

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
