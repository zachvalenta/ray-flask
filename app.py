from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
	return 'hey zv'


app.run(port=5000)
